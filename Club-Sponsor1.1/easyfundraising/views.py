from email import email
import json

from django.http import HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from .models import  User, UserDetail, Item


# Create your views here.
def  home(req):
    if req=='POST':
        email = req.POST['entry.1278961137']
        return render_to_response('html/login.html',
                              context_instance=RequestContext(req))
    return render(req, "html/home.html",)

def  login(req):

    if req.method=='POST':
        email = req.POST['email']
        password = req.POST['password']
        usr = User.objects.all().filter(email=email,password = password)
    
        if  usr:
            response = render_to_response('html/home.html',
                              context_instance=RequestContext(req))
            response .set_cookie("usermail",email,3600)
            response.set_cookie("username",usr[0].username,3600)
            
            
            return response
        else :
            return render_to_response('html/login.html',
                              context_instance=RequestContext(req))
    else :
        return render_to_response('html/login.html',
                              context_instance=RequestContext(req))
    
   
def  libray(req):
    items = Item.objects.all()[:5]
    return render(req,'html/library.html',)
def  register(req):
        if req.method == 'POST':
            name = req.POST['name']
            email = req.POST['email']
            password = req.POST['password']
            res= User.objects.get_or_create(username=name,email=email,password=password)
          
            if res:
                return render_to_response('html/registersuccess.html',
                              context_instance=RequestContext(req))
            else:
                return render_to_response('html/register.html',
                              context_instance=RequestContext(req))
                
        else:
            return render_to_response('html/register.html',
                              context_instance=RequestContext(req))
            
            
    
