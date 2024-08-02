from django.urls import path
from .views import home, navbar

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('nav/', navbar, name='navbar'),
]