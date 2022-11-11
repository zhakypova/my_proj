from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()


    def __str__(self):
        return self.name


class Work(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    postalZip = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return self.address


class Account(models.Model):
    pin = models.IntegerField()
    acc_num = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return self.acc_num

