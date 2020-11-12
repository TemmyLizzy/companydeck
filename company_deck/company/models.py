from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employ_Form(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    copname = models.CharField(max_length=250)
    jobtitle = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __unicode__(self):
        return self.fname



class Employ_Form2(models.Model):
    my_population = models.CharField(max_length= 200)
    job = models.CharField(max_length=128)
    employment = models.CharField(max_length=128)
    contract = models.CharField(max_length=128)

    def __unicode__(self):
        return self.my_population


class Employ_Form3(models.Model):
    rangeo = models.CharField(max_length = 200)
    amount1 =models.CharField(max_length = 200)
    amount2 = models.CharField(max_length = 200)
    per = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)


    def __unicode__(self):
        return self.rangeo

class Review(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    rating_figures = models.CharField( max_length=200)
    rating = models.IntegerField()
    location = models.CharField(max_length=200)
    work = models.CharField(max_length =500)
    work1 = models.CharField(max_length = 500)
    work2 = models.CharField(max_length = 500)
    work3 = models.CharField(max_length = 500)
    work4 = models.CharField(max_length = 500)
    loc1 = models.CharField(max_length = 500)
    loc2 = models.CharField(max_length = 500) 
    loc3 = models.CharField(max_length = 500)
    loc4 = models.CharField(max_length = 500)
    job1 = models.CharField(max_length = 500)
    job2 = models.CharField(max_length = 500)
    job3 = models.CharField(max_length = 500)
    description = models.TextField()
    url = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name



class Job(models.Model):
    title = models.CharField(max_length = 500)
    name = models.CharField(max_length = 500)
    company = models.CharField(max_length = 500)
    company2 = models.CharField(max_length = 500)
    company3 = models.CharField(max_length = 500)
    location = models.CharField(max_length = 500)
    amount = models.CharField(max_length = 500)
    amount2 = models.CharField(max_length = 500)
    amount3 = models.CharField(max_length = 500)
    requirements = models.TextField()
    requirements2 = models.TextField()
    requirements3 = models.TextField()
    details = models.TextField()
    url = models.CharField(max_length=200)
    url2 = models.CharField(max_length=200)
    url3 = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name