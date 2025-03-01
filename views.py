from django.shortcuts import render,redirect
from . import models

def home(request):
     return render(request,"masterpage.html")


def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        password=request.POST.get("password")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        address=request.POST.get("address")
        city=request.POST.get("city")
        role="student"
        try:
           obj=models.mstdata(name=name, mobile=mobile, email=email, password=password, gender=gender, dob=dob, address=address, city=city,role=role)
           obj.save()
           return render(request,"login.html")
        except Exception as a:
            print(a)
            return render(request,"register.html",{"output":"Duplicate not Allow!"})

    else:
        return render(request,"register.html")

def login(request):
     if request.method=="GET":
      return render(request,"login.html")
     else:
         email=request.POST.get('email')
         password=request.POST.get("password")
         result=models.mstdata.objects.filter(email=email, password=password)
         print(type(result))
         if(len(result)>0):
             role=result[0].role
             print("role=",role)
             if(role=="student"):
                 print("welcome student")
             else:
              return render(request,"login.html")
         else:
             print("invalid")
             return render(request,"login.html",{"output":"Invalid email or password"})
     return render(request, "login.html")
         