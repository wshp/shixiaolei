from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_list(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_list.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        post_form.save()
        return redirect('/')
    else:
        post_form = PostForm()
    return render(request, 'post_create.html', {'post_form': post_form})


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')


def post_update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, instance=post)
        post_form.save()
        return redirect('/')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'post_update.html', {'post_form': post_form})
