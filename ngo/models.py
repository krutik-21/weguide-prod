from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"

class State(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "State"


class Religion(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Religion"




class Gender(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Gender"

class Type(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Type"

class Category(models.Model):
    name = models.CharField(max_length=150,unique=True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"




#NGO Model

class NGO(models.Model):
    title = models.CharField(max_length=150 , unique = True)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True)
    state = models.ForeignKey(State,on_delete=models.DO_NOTHING,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,blank=True,null=True)
    religion = models.ForeignKey(Religion,on_delete=models.DO_NOTHING,blank=True,null=True)
    gender = models.ManyToManyField(Gender)
    stype = models.ForeignKey(Type,on_delete=models.DO_NOTHING,blank=True,null=True)
    eligibility = models.TextField(max_length=50000,blank=True,null=True)
    content = models.TextField(max_length = 50000,blank=True,null=True)
    updated_on = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150,blank=True)
    site_url = models.CharField(max_length=300,null=True,blank=True)
    contact = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    location = models.TextField(max_length = 50000,blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "NGO"


#creates slug from title before saving the object
def pre_save_bookbank_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_bookbank_receiver,sender=NGO)

#crowd source model
class CrowdSource(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    location = models.CharField(max_length=1000,null=True,blank=True)
    eligibility = models.TextField(max_length=1000,null=True,blank=True)
    contact = models.CharField(max_length=300,null=True,blank=True)
    desc = models.TextField(max_length=3000,null=True,blank=True)
    person_name = models.CharField(max_length=300,null=True,blank=True)
    person_email = models.CharField(max_length=300,null=True,blank=True)
    person_contact = models.CharField(max_length=10,null=True,blank=True)
    reviewed = models.BooleanField(null=True,blank=True,default=False)
    sub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "CrowdSource"


