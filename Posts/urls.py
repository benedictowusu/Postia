from django.urls import path
from .views import

app_name = "posts"

urlpatterns = [
    path('list/', articles, name='list'),
    path("<slug:slug>/", article_detail, name='detail')
]