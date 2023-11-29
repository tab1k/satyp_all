from users.views import *
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path("signin/", SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/', include('account.urls')),
]
