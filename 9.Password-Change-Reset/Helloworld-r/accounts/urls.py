#accounts/urls.py
from django.urls import path
from .views import SignUpView
from .views import change_password,reset_password
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/',change_password, name='password_change'),
    path('reset_password/',reset_password, name='reset_password'),
    
]
