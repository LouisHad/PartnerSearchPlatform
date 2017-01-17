from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.Dear Sonya,Good afternoon, I would send you more details after 25th of January
class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

class Programme(models.Model):
    programmeName=models.CharField(max_length=200)

    def __str__(self):
        return self.programmeName




class UserAttribute(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #institution= models.(Institution, on_delete=models.CASCADE,blank=True,null=True)
    fullname=models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.fullname

class Institution(models.Model):
    i_user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    institution_name = models.CharField(max_length=200)
    institution_department = models.CharField(max_length=200)
    # country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    erasmusCN = models.CharField(max_length=150) #ERASMUS Charter Number
    website = models.CharField(max_length=500)

    def __str__(self):
        return self.institution_name


class SubmitRequest(models.Model):
    sr_user = models.ForeignKey(User, on_delete=models.CASCADE)
    sr_institution=models.ForeignKey(Institution, on_delete=models.CASCADE, blank=False,null=False)
    sr_program = models.ForeignKey(Programme, on_delete=models.CASCADE, blank=False,null=False,default=None)
    # institution= models.ForeignKey(Institution, on_delete=models.CASCADE,blank=True,null=True)
    pic_number = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=150,blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    type_of_partners = models.CharField(max_length=500, blank=True, null=True)
    interest_Expected = models.DateField(help_text="Please use the following format: <em>DD-MM-YYYY</em>.", blank=True, null=True)
    deadline_call = models.DateField(help_text="Please use the following format: <em>DD-MM-YYYY</em>.",blank=True, null=True)

    SR_R = 'R'
    SR_I = 'A'
    SR_CHOICES = ((SR_R, 'Request'), (SR_I, 'Available'))
    type_of_Submit = models.CharField(max_length=2,
                              choices=SR_CHOICES,
                              default=SR_I)
    def __str__(self):
        return self.title


class UserInterestTo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_to = models.ForeignKey(SubmitRequest, on_delete=models.CASCADE)
    sr_program = models.ForeignKey(Programme, on_delete=models.CASCADE, blank=False,null=False,default=None)

def __str__(self):
        return self.user.username