from django.db import models

class Adult(models.Model):
    age = models.IntegerField(default=0)
    workclass = models.CharField(max_length=40)
    fnlwgt = models.IntegerField()
    education = models.CharField(max_length=40)
    education_num = models.IntegerField()
    marital_status = models.CharField(max_length=40)
    occupation = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)
    race = models.CharField(max_length=40)
    sex = models.CharField(max_length=40)
    capital_gain = models.IntegerField()
    capital_loss =  models.IntegerField()
    hours_per_week =  models.IntegerField()
    native_country = models.CharField(max_length=50)
    makes = models.CharField(max_length=20, blank=True)

