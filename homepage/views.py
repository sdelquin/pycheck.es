from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'homepage/index.html', context)
