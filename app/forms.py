from django import forms

from .models import Customer, Owner, Hotel

from functools import partial


class SignUpForm(forms.Form):
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    user_type = forms.ChoiceField(choices=((Customer, 'Customer'),
                                           (Owner, 'Owner')))
    username = forms.CharField(max_length=100)
    password = forms.CharField(min_length=6, max_length=32,
                               widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=6, max_length=32,
                                      widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=300)
    birth_date = forms.DateField(input_formats='%mm-$dd-%yyyy', widget=DateInput())
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    profile_image = forms.ImageField(required=False)    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        if password != repeat_password:
            raise forms.ValidationError('Passwords are not same')
        else:
            return cleaned_data


class HotelCreationForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_type', 'description', 'phone', 'location']
