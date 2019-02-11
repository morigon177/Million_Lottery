from django.shortcuts import render,redirect
from ML.models import Type, Song


def index(request):
    global values
    if(request.method == 'POST'):
       try:
           values = request.POST['type']
       except:
           values = '0'
       
       if(values == '1'):
            datal = Song.objects.filter(TypeName__TypeName__contains ='Princess' )
        
       elif(values == '2'):
            datal = Song.objects.filter(TypeName__TypeName__contains = 'Fairy')
        
       elif(values == '3'):
            datal = Song.objects.filter(TypeName__TypeName__contains = 'Angel')    
        
       elif(values == '4'):
            datal = Song.objects.filter(TypeName__TypeName__contains = 'All')    
       
       else:
            datal = Song.objects.filter(TypeName__TypeName__contains = 'abc')
       
       data = datal.order_by('?')[:1]     
       
    else:
        data = Song.objects.filter(TypeName__TypeName__contains = 'abc')
             
    params = {
        'title':"What's Next Song ?" ,
        'data':data,
    }
    

    return render(request, 'ML/index.html', params)