from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
    


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    prodId = models.CharField(max_length=90,default="0")
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=111,default="")
    address = models.CharField(max_length=111,default="")
    city = models.CharField(max_length=111,default="")
    state = models.CharField(max_length=111,default="")
    amount = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=111,default="")
    phone = models.CharField(max_length=111, default="")

