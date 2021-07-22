from django.shortcuts import render
from . import models

# Create your views here.

context = {'name':'70m R1ddl3', 'aka':'V01d3m0r7', 'special1':'Ethical Hack', 'special2':'Penetration Test'}

def Home(request):    
    return render(request, 'index.html', context)

def About(request):    
    return render(request, 'about.html', context)

def Works(request):    
    return render(request, 'works.html', context)

def Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        try:
            reason = request.POST['reason']
        except:
            reason=None
        message = request.POST['message']
        
        contact = models.Contact(name=name, email=email, reason=reason, message=message)
        contact.save()

    return render(request, 'contact.html', context)
