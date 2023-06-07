from django.db import models


class Referral(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class Driver(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    img = models.ImageField(upload_to='cdl')
    ref = models.ForeignKey(Referral, on_delete=models.CASCADE)
    dln = models.CharField(max_length=200, unique=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

