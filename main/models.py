from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title


class About_us(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='about_us/')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Special(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='special/')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Awards(models.Model):
    img = models.ImageField(upload_to='awards/')


class Emplayee(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='employee/')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField
    phone = models.CharField(max_length=13)
    last_name = models.CharField(max_length=255)
    massage = models.TextField()

    def __str__(self):
        return self.last_name


class Awards(models.Model):

    img = models.IntegerField

