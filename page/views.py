from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'page/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'page/post_detail.html', {'post': post})

def about(request):
    return render(request, 'page/about.html')

def business(request):
    return render(request, 'page/business.html')

def science(request):
    return render(request, 'page/science.html')

def product(request):
    return render(request, 'page/product.html')

def career(request):
    return render(request, 'page/career.html')

def plan(request):
    return render(request, 'page/plan.html')