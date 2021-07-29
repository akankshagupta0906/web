from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from WebDaity.models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Service,Plans,DelPlan,Blog
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate


# Create your views here.



def login_call(request): 
    if request.method=="POST":
       
        un=request.POST["username"]
        pwd=request.POST["password"]
        
        a=authenticate(username=un,password=pwd)
       
        
        if a:
            login(request,a)
            
            return redirect('/superuser/home/')
        
        else:
            return HttpResponse("<h1>invalid user and password</h1>")
    return render(request,"login.html")





@login_required
def logout_call(request):
	logout(request)
	return redirect('/superuser/login/')

@login_required(login_url='/home/')
def home(request):
    sobj = Service.objects.all()
    
    dobj = DelPlan.objects.all()
    return render(request,'superuser.html',{'sobj':sobj,'dobj':dobj})

def service(request):
    if request.method=="POST":
        serv=request.POST["service"]
        img=request.FILES["image"]
        
        sobj=Service(service=serv,img=img)
        sobj.save()
        
        return redirect('/superuser/service/')
    return render(request,'addservice.html')





def plan(request):
    if request.method=="POST":
        pn=request.POST["planname"]
        pmon = request.POST["pmonth"]
        pyear = request.POST["pyear"]
        year = request.POST["year"]
        mon = request.POST["month"]

        

        pobj=Plans(plan_name=pn,price_mon=pmon,price_year=pyear,month=mon,year=year)
        pobj.save()
        return redirect('/superuser/plan_del/')
        
    return render(request,'addplan.html')

def plan_del(request):
    plans=Plans.objects.all()
    if request.method=='POST':
        plan=request.POST["plan"]
        plan2=request.POST["plan2"]
        plan3=request.POST["plan3"]
        plan4=request.POST["plan4"]
        plan5=request.POST["plan5"]
        eid=request.POST['id']
        pobj = Plans.objects.get(id=eid)
        pobjs=[plan,plan2,plan3,plan4,plan5]
        for i in pobjs:
            dobj=DelPlan(plan=i,plan_n=pobj)
            dobj.save()
        return redirect('/superuser/plan_del/')
    return render(request,"addplandel.html",{'plans':plans})
        
def blog(request):
    if request.method=="POST":
        blon = request.POST["blogtitel"]
        blog = request.POST["blogger"]
        bobj = Blog(titel=blon,blog=blog)
        bobj.save()
        return redirect("/superuser/blog/")
    return render(request,"addblog.html")

def det(request,id):
    pobj = Plans.objects.get(id=id)
    dobj = DelPlan.objects.filter(plan_n=pobj)
    return render(request,"alldetails.html",{'dobj':dobj,'pobj':pobj})



