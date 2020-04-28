from __future__ import unicode_literals # 파이선 2.x 버전에서도 지원이 가능 하게 해준다 우리는 3.0
from django.db import models # 데이터베이스 연동
from django.utils.encoding import python_2_unicode_compatible # 아레와 같은말


# Create your models here.


@python_2_unicode_compatible
class Cityimage(models.Model):
    image = models.ImageField(blank=True, default=500)
    rank = models.IntegerField(default=32)
    name = models.TextField(blank=True)
    choice = models.IntegerField(default=0)

class Foodimage(models.Model):
    image = models.ImageField(blank=True, default=500)
    rank = models.IntegerField(default=32)
    name = models.TextField(blank=True)
    choice = models.IntegerField(default=0)

class Movieimage(models.Model):
    image = models.ImageField(blank=True, default=500)
    rank = models.IntegerField(default=32)
    name = models.TextField(blank=True)
    choice = models.IntegerField(default=0)

class Enterimage(models.Model):
    image = models.ImageField(blank=True, default=500)
    rank = models.IntegerField(default=32)
    name = models.TextField(blank=True)
    choice = models.IntegerField(default=0)


