from django.shortcuts import render, redirect
from django.views import View

from .forms import SignUpForm
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


