from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Books(models.Model):
    status_book=[
      ('availble','availble'),
      ('sold','sold'),
    ] 
     
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    photo_book=models.ImageField(upload_to='photos/',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photos/',null=True,blank=True)
    number_of_pages=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=status_book,null=True,blank=True)
    publish_date=models.DateTimeField()
    quantity=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
  
    
    def __str__(self):
        return self.title