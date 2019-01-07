
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

from product.models import Product
from product.models import Categories

from django.contrib.auth import authenticate
from django.contrib.auth.views import LogoutView


def userLogout(request):
    request.session['status'] = False
    request.session['name'] = ""
    p = Product.objects.all()
    c = Categories.objects.all()
    return render(request,"main/index.html",{"product": p, "category": c})


class UserViewByCategory(View):
    def get(self,request):
        cat = request.GET.get("cat")
        p = Product.objects.filter(categorieName=cat)
        c = Categories.objects.all()
        return render(request, "customer/home.html", {"product": p, "category": c})



class UserIndexPage(View):
    def get(self,request):
        p = Product.objects.all()
        c = Categories.objects.all()
        items = len(request.COOKIES)
        return render(request,"customer/home.html",{"product":p,"category":c,"items":items})



def validateUser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    au = authenticate(username=username,password=password)

    if au is not None:
        request.session['status'] = True
        request.session['name'] = username
        p = Product.objects.all()
        c = Categories.objects.all()
        q = CCItems.objects.filter(name=username)
        items = len(q)
        return render(request,"customer/home.html",{"form":au,"product": p, "category": c,"items":items})
    else:
        print("Invalid")
    return render(request, "registration/login.html",{"message":"Invalid Details"})

def userLogin(request):
    return render(request,"registration/login.html")



def userCreation(request):
    uc = UserCreationForm(request.POST)
    if request.method == "POST":
        if uc.is_valid():
            uc.save()
            return redirect('/user/')
        else:
            return render(request, "registration/register.html", {"form": uc})
    else:
        uc = UserCreationForm()
        return render(request,"registration/register.html",{"form":uc})

class IndexPage(View):
    def get(self,request):
        p = Product.objects.all()
        c = Categories.objects.all()
        items = len(request.COOKIES)
        return render(request,"main/index.html",{"product":p,"category":c,"items":items})

class ViewByCategory(View):
    def get(self,request):
        cat = request.GET.get("cat")
        p = Product.objects.filter(categorieName=cat)
        c = Categories.objects.all()
        return render(request, "main/index.html", {"product": p, "category": c})

from customer.models import CCItems
def addToCart(request):
    key = request.GET.get("key")
    p = Product.objects.all()
    c = Categories.objects.all()

    status = request.session['status']
    name = request.session['name']
    if status:
        c1 = CCItems(name=name,pid=key)
        c1.save()
        q = CCItems.objects.filter(name=name)
        items = len(q)
        return render(request,'customer/home.html',{"product":p,"category":c,"items":items,"form":name})
    else:
        items = len(request.COOKIES)
        response = render(request,"main/index.html",{"product":p,"category":c,"items":items})
        response.set_cookie(key,key)
        return response


