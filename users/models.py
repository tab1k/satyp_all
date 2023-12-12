import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from  django.core.mail import send_mail


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский'), ('other', 'Другой')],
                              blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    is_verified_email = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class EmailVerification(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object: {self.user.email}'


    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Test verification email",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )