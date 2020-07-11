from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from .decorators import owner_required
from .forms import SignUpForm, HotelCreationForm
from .models import User


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/signup')


class HotelCreation(View):
    @login_required
    @owner_required
    def get(self, request):
        form = HotelCreationForm()
        return render(request, 'hotel_creation.html', {'form': form})

    @login_required
    @owner_required
    def post(self, request):
        form = HotelCreationForm(request.POST)
        if form.is_valid():
            hotel_pk = form.save()
            return redirect('/hotel/{}'.format(hotel_pk))
        else:
            return render(request, 'hotel_creation.html', {'form': form})
