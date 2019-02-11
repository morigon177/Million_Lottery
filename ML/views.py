from django.shortcuts import render
from .models import Type, Song


def index(request):
    params = {
        'title':"What's Next Song ? " ,
        }
    
    if(request.method == 'POST'):
        values = request.POST.getlist('type')
    
    return render(request, 'ML/index.html', params)