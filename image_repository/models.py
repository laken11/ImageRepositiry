from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=20, verbose_name='image name')
    tag = models.CharField(max_length=20, verbose_name='tag on the image', default=name)
    tag2 = models.CharField(max_length=20, verbose_name='tag on the image', null=True, blank=True)
    tag3 = models.CharField(max_length=20, verbose_name='tag on the image', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, verbose_name='description of the image')
    owner = models.ForeignKey('Owner', on_delete=models.RESTRICT, verbose_name='the owner of the image')
    image = models.ImageField()


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT,
                                verbose_name='django user model object related to owner class')
    info = models.CharField(max_length=50, null=True, verbose_name='Information about the user uploading image')

