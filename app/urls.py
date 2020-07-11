from django.urls import path
from .views import SignUpView, HotelCreation

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('hotel/add', HotelCreation.as_view()),
]