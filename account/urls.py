from account.views import UserProfileView
from django.urls import path

app_name = 'account'

urlpatterns = [
    path("profile/<int:pk>/", UserProfileView.as_view(), name='profile'),
]
