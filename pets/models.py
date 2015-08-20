from django.db import models
from django.conf import settings

class Pet(models.Model):

    GENDERS =[
        ('m',"Male"),
        ('f',"Female"),
    ]
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    kind = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDERS)
    is_barren = models.BooleanField(default=False)
    image = models.URLField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    location = models.CharField(max_length=50)

    pet = models.ForeignKey('Pet', related_name='posts',null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null= True)

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receipt_messages')
    subject = models.CharField(max_length=50)
    body = models.TextField()
    is_read = models.BooleanField(default=False)



