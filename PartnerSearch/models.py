from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Institution(models.Model):
    institution_name=models.CharField(max_length=500)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=150)
    erasmusCN=models.CharField(max_length=150) #ERASMUS Charter Number
    website = models.CharField(max_length=500)

    def __str__(self):
        return self.institution_name


class Programme(models.Model):
    programmeName=models.CharField(max_length=200)

    def __str__(self):
        return self.programmeName


# Create your models here.
class UserAttribute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution= models.ForeignKey(Institution, on_delete=models.CASCADE,blank=True,null=True)
    fullname=models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.fullname


class SubmitRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # institution= models.ForeignKey(Institution, on_delete=models.CASCADE,blank=True,null=True)
    interest_Expected = models.DateField(help_text="Please use the following format: <em>DD-MM-YYYY</em>.")
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.institution


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_to = models.ForeignKey(SubmitRequest, on_delete=models.CASCADE)

