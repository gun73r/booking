from django import forms
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.db import IntegrityError


from .models import Customer, Owner, Hotel, Image
from booking import settings

from functools import partial
from datetime import datetime


class SignUpForm(forms.Form):
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    user_type = forms.ChoiceField(choices=(('customer', 'Customer'),
                                           ('owner', 'Owner')))
    username = forms.CharField(max_length=100)
    password = forms.CharField(min_length=6, max_length=32,
                               widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=6, max_length=32,
                                      widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=300)
    birth_date = forms.DateField(input_formats=('%m/%d/%Y',), widget=DateInput())
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    profile_image = forms.ImageField(required=False)

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if password != repeat_password:
            self.add_error('repeat_password', 'Passwords must match')

    def save(self):
        cd = self.cleaned_data
        username = cd.get('username')
        password = cd.get('password').encode('utf-8')
        password_hash = PBKDF2PasswordHasher().encode(password,
                                                      settings.SECRET_KEY)
        full_name = cd.get('full_name')
        birth_date = cd.get('birth_date')
        email = cd.get('email')
        phone = cd.get('phone')
        image = cd.get('profile_image')

        user = None
        try:
            if cd.get('user_type') == 'customer':
                user = Customer(username=username, password=password_hash,
                                full_name=full_name, birth_date=birth_date, email=email,
                                phone=phone)
            elif self.cleaned_data.get('user_type') == 'owner':
                user = Owner(username=username, password=password_hash,
                             full_name=full_name, birth_date=birth_date, email=email,
                             phone=phone)
            if user is not None and image is not None:
                image = Image(photo=image, pub_date=datetime.now())
                user.profile_image = image
                image.save()
            user.save()
        except IntegrityError:
            self.add_error('image', 'all fields should be unique')


class HotelCreationForm(forms.ModelForm):
    def save(self, **kwargs):
        cd = self.cleaned_data
        name = cd.get('name')
        hotel_type = cd.get('hotel_type')
        location = cd.get('location')
        description = cd.get('description')
        phone = cd.get('phone')
        hotel = Hotel(name=name, hotel_type=hotel_type, location=location, description=description, phone=phone)
        hotel.save()
        return hotel

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_type', 'description', 'phone', 'location']
