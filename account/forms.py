from django import forms
from django.contrib.auth.forms import UserChangeForm
from users.models import CustomUser


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'age')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['phone_number'].widget.attrs['class'] = 'form-control'
            self.fields['age'].widget.attrs['class'] = 'form-control'


