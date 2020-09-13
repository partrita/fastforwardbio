from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'page/index.html', context)

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