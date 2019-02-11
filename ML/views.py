from django.shortcuts import render
from ML.models import Type, Song


def index(request):
    global data
    if(request.method == 'POST'):
        values = request.POST.getlist('type')
       
        if(values == '1'):
            data = Song.objects.filter(TypeName__iexact ='Princess' )
        
        elif(values == '2'):
            data = Song.objects.filter(TypeName__iexact = 'Fairy')
        
        elif(values == '3'):
            data = Song.objects.filter(TypeName__iexact = 'Angel')    
        
        elif(values == '4'):
            data = Song.objects.filter(TypeName__iexact = 'All')
    
    else:
        #values = request.POST.getlist('type')
        data = Song.objects.all()
             
    params = {
        'title':"What's Next Song ? " ,
        'data':data,
    }
    

    return render(request, 'ML/index.html', params)