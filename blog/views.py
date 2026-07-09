from django.shortcuts import render, redirect
from django.contrib import messages

from blog.forms import PostForm
from blog.models import Post
from django.utils import timezone
from django.conf import settings

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
        else:
            messages.error(request, form.errors)
    form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def post_edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect("/admin/login/")
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(request.user)
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
        else:
            messages.error(request, form.errors)
    form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})