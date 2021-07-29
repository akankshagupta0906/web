from django.shortcuts import render,redirect
from superuser.models import Service,DelPlan,Plans

def home(request):
    
    pobjs = Plans.objects.all()
    sobj = Service.objects.all()
    
    
    return render(request,"index.html",{'sobj':sobj,'pobjs':pobjs})

def allBlog(request):
    bobjs = Blog.objects.all()
    return render(request,"blog.html",{'bobjs':bobjs})

def det(request,id):
    pobj = Plans.objects.get(id=id)
    dobj = DelPlan.objects.filter(plan_n=pobj)
    return render(request,"alldetails.html",{'dobj':dobj,'pobj':pobj})
