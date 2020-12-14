from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=250)


    def __str__(self):
        return self.name

class Massege(models.Model):
    msg_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False, null=True)
    email_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='email_to')
    email_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='email_by')
    subject = models.TextField()
    file = models.FileField(upload_to='file')

    def __str__(self):
        return self.email_by.name



