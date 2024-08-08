from django.urls import path
from .views import Posts, post_details

app_name = 'post'

urlpatterns = [
    path('', Posts, name='posts'),
    path("<slug:slug>/", post_details, name='detail')
]