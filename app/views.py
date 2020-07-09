from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from .decorators import owner_required
from .forms import SignUpForm, HotelCreationForm
from .models import User


class SignUpView(View):
    def get(self, request):
        form = SignUpForm(request.POST)
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        form.clean()
        print(form.errors)
        return redirect('/signup')


# @login_required
# @owner_required
class HotelCreation(View):
    def get(self, request):
        form = HotelCreationForm()
        return render(request, 'hotel_creation.html', {'form': form})

    def post(self, request):
        form = HotelCreationForm(request.POST)
        return render(request, 'hotel_creation.html', {'form': form})
