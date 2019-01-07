"""ECPCoding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import DetailView

from ECPCoding import settings
from django.contrib.auth import views as ll

from main.views import IndexPage
from main.views import ViewByCategory
from main.views import userCreation
from main.views import addToCart
from main.views import userLogin
from main.views import validateUser
from main.views import UserIndexPage
from main.views import UserViewByCategory
from main.views import userLogout
from main.views import openCart
from main.views import removeFromCart


from product.models import Product

urlpatterns = [
    #admin urls
    path('admin/', admin.site.urls),

    #users
    path('user/',userLogin),
    path('register/',userCreation),
    path('validateUser/',validateUser),
    path('userlogout/',userLogout),
    path('opencart/',openCart),
    path('removefromcart/',removeFromCart),
    path('userhome/',UserIndexPage.as_view()),
    path('usersearch/',UserViewByCategory.as_view()),

    #main urls
    path('home/',IndexPage.as_view()),
    path('addtocart/',addToCart),
    path('productdetails<int:pk>/',DetailView.as_view(template_name="main/product_detials.html",model=Product)),
    path('search/',ViewByCategory.as_view()),

    #product urls



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

