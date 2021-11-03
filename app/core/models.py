from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dni = models.CharField(max_length=255, unique=True)
    nationality = models.CharField(max_length=255)
    birth_date = models.DateField()
    username = models.CharField(max_length=255, unique=True)
    enrollment = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'