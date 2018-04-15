from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def list_post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    template = 'blog/list.html'

    return render(request, template, context)


def create_post(request):
    pass


def delete_post(request):
    pass


def update_post(request):
    pass


def detail_post(request):
    pass
