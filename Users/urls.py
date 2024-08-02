from django.urls import path
from .views import Signin, signup

app_name = 'Users'

urlpatterns = [
    path('signin/', Signin, name='signin'),
    path("signup/", signup, name='signup' ),
]