from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib.contenttypes.models import ContentType
from .models import Post
from blog.forms import PostForm
from django.contrib import messages
from comments.forms import CommentForm
from comments.models import Comment

# Create your views here.
def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def list_post(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    template = 'blog/list.html'
    return render(request, template, context)


def create_post(request):
    if not request.user.is_staff or not request.user.is_active:
        raise Http404
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/blog')
        messages.success(request, "Successfullt created.")
    else:
        form = PostForm()
    context = {
        'form': form
    }
    template = 'blog/form.html'
    return render(request, template, context)


def delete_post(request, slug):
    if not request.user.is_staff or not request.user.is_active:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect('/blog/')


def update_post(request, slug):
    if not request.user.is_staff or not request.user.is_active:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        messages.success(request, 'blog details updated.')
        return redirect('/blog')
    else:
        form = PostForm(instance=instance)
    context = {
        'instance': instance,
        'form': form
    }
    template = 'blog/form.html'
    return render(request, template, context)


def detail_post(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    template = 'blog/detail.html'
    comments = instance.comment

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        object_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get('comment')

        new_comment, created = Comment.objects.create(
            user = request.user,
            content_type =content_type,
            object_id = object_id,
            comment = content_data
        )

        if created:
            print('It has been created')
    context = {
        'instance': instance,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, template, context)
