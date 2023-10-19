from django.db import models


class Premier(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='premier')


class Popular(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='popular')


class Recent(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recent')


class Film(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='film')


class Tv(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tv')


class Comment(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='comment')


class Hero(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    show = models.CharField(max_length=100)
    new = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hero')


class Review(models.Model):
    name = models.CharField(max_length=100)
    time = models.FloatField()
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='review')


class Disk(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='disk')
