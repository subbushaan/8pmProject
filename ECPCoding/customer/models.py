from django.db import models

class CCItems(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pid = models.IntegerField()
