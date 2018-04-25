from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages


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


def delete_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    return redirect('/blog/')


def update_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
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


def detail_post(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)

    template = 'blog/detail.html'
    context = {
        'instance': instance
    }

    return render(request, template, context)
