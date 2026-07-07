from django.shortcuts import render

from blog.forms import PostForm
from blog.models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

