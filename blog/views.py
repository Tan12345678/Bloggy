from datetime import timezone

from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts, 'query': query})
# blog/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # Set pub_date to the current date and time
            post.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')

def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/view_post.html', {'post': post})