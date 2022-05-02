from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('contact/',views.contact,name='ContactUs'),
    path('about/',views.about,name='AboutUs'),
    path('products/',views.products,name='Products'),
    path('single_product/',views.single_product,name='Single_product'),
]