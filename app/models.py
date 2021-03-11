from django.db import models

# Create your models here.


class Addess(models.Model):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=120)
    addess = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.phone


class Slider(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    date = models.DateField()

    img = models.ImageField(upload_to="slider/img", default="")

    def __str__(self):
        return self.title1


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    img = models.ImageField(upload_to="recipes", default="")
    date = models.DateField()

    def __str__(self):
        return self.name


class About(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=150)
    desc2 = models.CharField(max_length=150)
    img = models.ImageField(upload_to="adout", default="")
    date = models.DateField()

    def __str__(self):
        return self.title1


class Blocktitle(models.Model):
    blocktitle = models.CharField(max_length=100)
    blockdesc = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.blocktitle


class Blog(models.Model):

    title = models.CharField(max_length=100)

    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to="block", default="")
    date = models.DateField()

    def __str__(self):
        return self.title


class Client(models.Model):

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to="client", default="")
    date = models.DateField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    newsletteremail = models.CharField(max_length=120)

    def __str__(self):
        return self.newsletter
