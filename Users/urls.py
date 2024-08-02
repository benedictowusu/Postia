from django.urls import path
from .views import Signin, signup

urlpatterns = [
    path('signin/', Signin, name='signin'),
    path("signup/", signup, name='signup' ),
]