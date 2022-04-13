from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:myid>', views.productView, name='ProductView'),
    path('buy/<int:myid>', views.BuyView, name='BuyView'),
    path('products/<int:myid>/TryNow/', views.TryNow , name="TryNow"),
    path('checkout/',views.checkout,name="checkout"),
    path('about_us',views.AboutUs,name="about us"),
    path('contacts',views.ContactUs,name="Contact us"),
]
