from django.db import models


# Create your models here.
class Branch(models.Model):
    Bname=models.CharField(max_length=250)
    SubBranch1=models.CharField(max_length=250)
    SubBranch2=models.CharField(max_length=250)

    def __str__(self):
        return self.Bname


class book(models.Model):
    name=models.CharField(max_length=250)
    adress=models.CharField(max_length=250)
    Email=models.EmailField()
    phone=models.IntegerField()
    category=models.ForeignKey(Branch,on_delete=models.CASCADE)
    flower=models.ForeignKey('shop.Flower',on_delete=models.CASCADE)
    Quantity=models.IntegerField()

    def __str__(self):
        return self.name

