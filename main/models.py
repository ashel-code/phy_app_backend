from django.db import models

# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=31, primary_key=True)
    hash = models.CharField(max_length=255)
    def __int__(self):
        return self.login

    status = models.IntegerField(default=0)

class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=16384)
    endUser = models.ForeignKey(Users, on_delete=models.CASCADE)
    primaryUser = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


