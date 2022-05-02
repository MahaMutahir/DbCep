from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'dbcep/index.html')

def products(request):
    products1=Lip_color.objects.all()
    products2=Setting_spray_powder.objects.all()
    products3=Primer.objects.all()
    products4=Foundation.objects.all()
    products5=Highlighter.objects.all()
    products6=CC_Cream.objects.all()
    products7=Eyeshadow.objects.all()
    products8=Concealer.objects.all()
    products9=Blush.objects.all()
    products10=Bronzer.objects.all()
    products11=Eyebrow_pencil.objects.all()
    products12=Mascarra.objects.all()
    products13=Eyeliner.objects.all()
    
    


    context={'products1':products1,
             'products2':products2,
             'products3':products3,
             'products4':products4,
             'products5':products5,
             'products6':products6,
             'products7':products7,
             'products8':products8,
             'products9':products9,
             'products10':products10,
             'products11':products11,
             'products12':products12,
             'products13':products13,
             
             
            
            }
    return render(request, 'dbcep/products.html',context)

def about(request):
    return render(request,'dbcep/about.html')

def contact(request):
    return render(request,'dbcep/contact.html')

def single_product(request):
    object=Cart.objects.all()[0]
    context={'object':object}
    return render(request,'dbcep/single_product.html',context)
