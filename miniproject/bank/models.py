from django.db import models

# Create your models here.
class bank (models.Model):
    name=models.CharField(max_length=30)
    acc_no=models.IntegerField(unique=True)
    amount=models.IntegerField()
    phno=models.IntegerField()

    def __str__(self):
          return self.name