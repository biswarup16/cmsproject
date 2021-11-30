from django.db import models

# Create your models here.

class Carousel(models.Model):
    image       = models.ImageField(upload_to="banner")
    title       = models.CharField(max_length=150)
    # action_name = models.CharField(max_length=50)
    # link        = models.TextField(null=True, blank=True)
    # sub_title   = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Cards(models.Model):
    photo       = models.ImageField(upload_to="cards")
    description       = models.CharField(max_length=150)

    # title       = models.CharField(max_length=150)
    # action_name = models.CharField(max_length=50)
    # link        = models.TextField(null=True, blank=True)
    # sub_title   = models.CharField(max_length=100)
    def __str__(self):
        return self.description

class About(models.Model):
    aboutpic = models.ImageField(upload_to="about")
    aboutdesc = models.TextField()        

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    document = models.FileField(upload_to="files",blank=True)
    desc = models.TextField()
    # contactimage = models.ImageField(upload_to="contactmedia")
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Photogallery(models.Model):
    photogallery = models.ImageField(upload_to="about")
    phototitle = models.CharField(max_length=30)
    def __str__(self):
        return self.phototitle

