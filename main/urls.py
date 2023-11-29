from main.views import *
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
