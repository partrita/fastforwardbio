from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'page/index.html', context)