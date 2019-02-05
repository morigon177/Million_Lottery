from django.shortcuts import render
from .models import Type, Song


def index(request):
    params = {
        'title':"What's Next Song ? " ,
        }
    return render(request, 'ML/index.html', params)