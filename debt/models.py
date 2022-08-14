from unicodedata import name
from django.db import models

class owes_Model(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    class Meta:
        verbose_name_plural = ("Owes")

    def __str__(self):
        return self.name 


class owed_by_Model(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()    

    class Meta:
        verbose_name_plural =("Owed_by")

    def __str__(self):
        return self.name


class USer_Model(models.Model):
    name = models.CharField(max_length=50)
    owes = models.ManyToManyField(owes_Model)
    owed_by = models.ManyToManyField(owed_by_Model)
    balance = models.FloatField(null= True)

    class Meta:
        verbose_name_plural = ("Users list")

    def __str__(self):
        return self.name


class Debt_model(models.Model):
    lender = models.CharField(max_length=50)
    borrower = models.CharField(max_length=50)
    amount = models.FloatField()

    class Meta:
        verbose_name_plural = ("Debt List")

    def __str__(self):
        return self.lender