from django.db import models

class Categories(models.Model):
    categorieName = models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.categorieName

class Product(models.Model):
    idno = models.AutoField(primary_key=True)
    categorieName = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product/%y%m%d')
    message = models.TextField()

    def __str__(self):
        return self.name