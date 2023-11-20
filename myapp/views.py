from django.shortcuts import render
from .models import *


def portfolio(request):
    if request.POST:    
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        usermessage = request.POST.get('usermessage')
        dataSave = text( username=username ,useremail=useremail ,usermessage=usermessage)
        dataSave.save()
    
    context = {
    'me' : Me.objects.all(),
    'hobby' : Hobby.objects.all(),
    'video' : Video.objects.all(),
    'message' : text.objects.all(),
    'slide' : Slide.objects.all(),
    'link' : Link.objects.all(),
    }

    return render(request, 'myapp/portfolio.html', context)