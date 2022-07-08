# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from enum import auto
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = [] 
    role_choice = ((0, "Guest"),(1,"Employee"),(2,"Warehouse Master"),(3,"Boss"),(4,"SUPER USER"))
    role = models.IntegerField(choices = role_choice, default=0)

class AllSparePart(models.Model):
    class Status(models.TextChoices):
        good = 'Good'
        new = 'New'
        fail = 'Fail'
        scrap = 'Scrap'
        other =  'Other'

    class SpareType(models.TextChoices):
        product = 'Product'
        sparePart = 'Spare'
        other = 'Other'

    class CSCEHWMO(models.TextChoices):   
        central = 'Central inverter'
        string = 'string inverter'
        commu = 'Comunication device'
        ess = 'ESS'
        hybrid = 'Hybird  inverter'
        wind = ' wind Converter'
        mv = 'MV device'
        other = 'Other'
    
    class WAREHOUSE(models.TextChoices):
        HN = 'HN'
        DN = 'DN'
        KH = 'KH'
        HCM = 'HCM'
        other = 'Other'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    partCode = models.CharField(max_length=10, null=True, blank=True)
    goodStatus = models.CharField(max_length=5, choices=Status.choices, default=None)
    sparePartType = models.CharField(max_length=7, choices=SpareType.choices, default=None)
    csceHWMO = models.CharField(max_length=20, choices=CSCEHWMO.choices,default=CSCEHWMO.other)
    serialNumber = models.CharField(max_length=20, null=True, blank=True, default=None)
    productDescription = models.CharField(max_length=100, null=True, blank=True)
    deliverDate = models.DateField(max_length=10, null=True, blank=True)
    warehouse = models.CharField(max_length=5, choices=WAREHOUSE.choices,default=None)
    sender = models.CharField(max_length=20, null=True, blank=True)
    invoice = models.CharField(max_length=20, null=True, blank=True)
    batch = models.CharField(max_length=20, null=True, blank=True)
    transitWay = models.CharField(max_length=20, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)

    actualQTY = models.IntegerField(null=False, blank=False)
    consumQTY = models.IntegerField(null=False, blank=False)
    remainQTY = models.IntegerField(null=False, blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def consum(self,n):
        self.consumQTY += n
        self.remainQTY -= n   

    
    def __str__(self):
        return f"{self.id,{self.partCode},{self.serialNumber}}"

class SparePartOutRequest(models.Model):
    id = models.AutoField(primary_key=True)
    userOutRequestor = models.ForeignKey(User, on_delete=models.CASCADE)
    sparePartOut = models.ForeignKey(AllSparePart, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    outqty = models.IntegerField(null=True, blank=True)
    outDate = models.DateField(null=True, blank=True)
    outReceiver = models.CharField(max_length=20, null=True, blank=True)
    outRemark = models.CharField(max_length=20, null=True, blank=True)
    file = models.FileField(upload_to='filerequest', null=True)

    # role_choice = ((0, "Waitting"),(1,"Submited by boss"),(2,"Submited by warehouse master"))
    # role = models.IntegerField(choices = role_choice, default=0)
    submitByBoss = models.BooleanField(default=False)
    submitByWm = models.BooleanField(default=False)
    gsp = models.CharField(max_length=20, null=True, blank=True)
    gspuser = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return f"{self.id,{self.submitByBoss},{self.submitByWm}}"

class SparePartOutRecord(models.Model):
    id = models.AutoField(primary_key=True)
    userOutRequestor = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    sparePartGoodOut = models.ForeignKey(AllSparePart, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    outqty = models.IntegerField(null=True, blank=True)
    outDate = models.DateField(null=True, blank=True)
    outReceiver = models.CharField(max_length=20, null=True, blank=True)

    outgsp = models.CharField(max_length=20, null=True, blank=True)
    gspuser = models.CharField(max_length=20, null=True, blank=True)

    outRemark = models.CharField(max_length=20, null=True, blank=True)
    file = models.FileField(upload_to='filerecord', null=True)
    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return str(self.id)


class Upload(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='fileupload', null=False)

    class Meta:
        ordering = ['-updated', '-created']
 
    def __str__(self):
        return str(self.id)