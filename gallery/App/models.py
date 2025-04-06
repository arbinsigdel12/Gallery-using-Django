from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30,blank=False, null=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    image=models.ImageField(null=False,blank=False)
    description=models.CharField(max_length=500,blank=False,null=False)

    def __str__(self):
        return self.description
    