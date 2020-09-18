from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    product_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="store/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=50, default="")
    descdata = models.CharField(max_length=300,default="")



    def __str__(self):
        return self.name