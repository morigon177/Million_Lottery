from django.shortcuts import render
#from .forms import IndexForm
from .models import Type, Song


def index(request):
    params = {
        'title':"What's Next Song ? " ,
        }
    
    if(request.method == 'POST'):
        values = request.POST.getlist('type')
        print(values)
    
    return render(request, 'ML/index.html', params)