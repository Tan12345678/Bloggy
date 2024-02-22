from datetime import timezone

from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts, 'query': query})
# blog/views.py
from django.shortcuts import  redirect,get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
@login_required(login_url='login')
def create_post(request):
    myflag=True
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # Set pub_date to the current date and time
            post.save()
            return redirect('index')
        else:
            return render (request,'blog/login.html',{'myflag' : myflag})
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
@login_required(login_url='login')
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')

def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/view_post.html', {'post': post})
def contact_us(request):
    return render(request,'blog/contact_us.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})\
        
def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})