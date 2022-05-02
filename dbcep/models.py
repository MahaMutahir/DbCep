from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=11,primary_key=True)
    contact = models.IntegerField(null=True)
    email = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=20,null=False)

class Product(models.Model):
    users=models.ForeignKey(Users,on_delete=models.CASCADE)
    product_id =models.AutoField(primary_key=True)
    product_name =models.CharField(max_length=50,null=False)
    product_quantity=models.IntegerField()
    price = models.CharField(max_length=10,null=False)
    



class Cart(models.Model):
    users=models.ForeignKey(Users,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_id =models.AutoField(primary_key=True)
    total_products=models.IntegerField(null=True)
    total_price=models.IntegerField()

class Order(models.Model):
    order_id =models.AutoField(primary_key=True)
    customer_id = models.IntegerField(null=False)
    contact =models.IntegerField(null=False)
    address =models.CharField(max_length=100,null=False)
    zipcode = models.CharField(max_length=100,null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)

    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)


class Lip_color(models.Model):
    product_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    type =models.CharField(max_length=100,null=False)
    matte_glossy=models.CharField(max_length=100,null=False)
    



class Added_to(models.Model):
    
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)

class Setting_spray_powder(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    F_product_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100,null=False)
    purpose_benefit =models.CharField(max_length=11, null=False)
    effect =models.CharField(max_length=100,null=False)

class Primer(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    F_product_id = models.AutoField(primary_key=True)
    skin_type = models.CharField(max_length=100,null=False)
    purpose_benefit =models.CharField(max_length=11, null=False)
    
class Foundation(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=False)
    shade =models.IntegerField(null=False)
    skin_type =models.CharField(max_length=100,null=False)

class Highlighter(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    single_pallette = models.CharField(max_length=10,null=False)

class CC_Cream(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    skin_type = models.CharField(max_length=100,null=False)
    shade =models.IntegerField(null=False)

class Concealer(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=False)
    shade =models.IntegerField(null=False)

class Highlighter_shades(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    shade = models.CharField(max_length=100,null=False)

class Blush(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=False)
    shade =models.IntegerField(null=False)

class Bronzer(models.Model):

    F_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    shade = models.CharField(max_length=100,null=False)



class Eyebrow_pencil(models.Model):

    E_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    

class Eyeshadow_color(models.Model):

    E_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    

class Eyeshadow(models.Model):

    E_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    single_pallette = models.CharField(max_length=100,null=False)

class Eyeliner(models.Model):

    E_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    

class Mascarra(models.Model):

    E_product_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='lip_color/')
    color =models.CharField(max_length=100)
    purpose_benefit =models.CharField(max_length=100,null=False)


