from django.db import models
from django.contrib.auth.models import User as DjangoUser


class Image(models.Model):
    photo = models.ImageField()
    pub_date = models.DateTimeField()


class User(DjangoUser):
    TYPES = [
        ('OWNER', 'Owner'),
        ('CUSTOMER', 'Customer'),
    ]
    user_type = models.CharField(max_length=10, choices=TYPES)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    credit_card = models.CharField(max_length=4, blank=True)
    profile_image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    rate = models.PositiveSmallIntegerField()
    photos = models.ForeignKey(Image, on_delete=models.CASCADE)


class Apartments(models.Model):
    TYPES = [
        ('Room', 'Room'),
        ('Number', 'Number'),
        ('Apartments', 'Apartments'),
        ('Hostel_Room', 'Hostel room'),
    ]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    photos = models.ForeignKey(Image, on_delete=models.CASCADE)
    cost = models.CharField(max_length=50)
    room_amount = models.PositiveSmallIntegerField()
    livers_amount = models.PositiveSmallIntegerField()
    description = models.TextField()
    apartments_type = models.CharField(max_length=50, choices=TYPES)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    phone = models.CharField(max_length=20)


class Order(models.Model):
    settlement_date = models.DateField()
    eviction_date = models.DateField()
    apartments = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Hotel(models.Model):
    TYPES = [
        ('ht', 'Hotel'),
        ('mt', 'Motel'),
        ('ap', 'Apartments'),
        ('hs', 'Hostel'),
    ]
    name = models.CharField(max_length=200)
    hotel_type = models.CharField(max_length=50, choices=TYPES)
    location = models.CharField(max_length=50)
    apartments = models.ForeignKey(Apartments, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
