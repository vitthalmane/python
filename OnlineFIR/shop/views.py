from django.shortcuts import render
from django.http import HttpResponse
from .models import userdata

# Create your views here.
def index(request):
    return render(request,"shop/index copy.html")

def ecomp(request):
    return render(request,"shop/index.html")

def getecomp(request):
    email=request.POST.get('uname','default')
    passw=request.POST.get('psw','default')
   
    obj=userdata.objects.all()
    for i in obj:
        if i.email==email:
            if i.password==passw:
                return render(request,'shop/register.html')
    return HttpResponse("User data not Found")
def regis(request):
    return render(request,"shop/registration.html")

def store(request):
    fname=request.POST.get('fname','default')
    fname=request.POST.get('lstname','default')
    email=request.POST.get('email','default')
    if request.POST.get('psw','default')==request.POST.get('psw-repeat','default'):
        psw=request.POST.get('psw','default')
        obj=userdata(fstname=fname,lstname='das',password=psw,email=email)
        obj.save()
        return HttpResponse("Register")
        return render(request,"shop/index.html")
    else:
        para={'name':"Password does not match"}
        return render(request,"shop/registration.html",para)
        



def upload(request):
    print("requet handled")
   # print(request.FILES['image'])
    p=request.FILES['image']
    print(str(p))
    import re
    if re.search("pdf$",str(p)) or re.search("png$",str(p)) or re.search("jpg$",str(p)) or re.search("jpeg$",str(p)):
        print("yess")
    #print(request.)
        from .models import fir
        #image=models.ImageField(upload_to='fir')
        name=request.POST.get('fstname','default') +request.POST.get('lstname','default')
        print(name)
        image=fir(img=p,name=name,addr=request.POST.get('addr','default'),
                    firstation=request.POST.get('station','default'),firtype=request.POST.get('firtype','default'
                    ),firdesc=request.POST.get('firdesc','default'))
        image.save()
        return HttpResponse("Completed")
    else:
        para={'name':"Not specified image format"}
        return render(request,"shop/register.html",para)