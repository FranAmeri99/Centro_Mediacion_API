from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.utils import timezone
import datetime


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Cretats and saves a new user"""
        if not email:
            raise ValueError("users must have an email addres")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def creat_super_user(self, email, password, enrollment):
        """Create and sabves new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.enrollment = enrollment
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email insted of username"""   
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    dni = models.CharField(max_length=255, unique=True)
    nationality = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255) #DateField() Preguntar a javi
    username = models.CharField(max_length=255, unique=True)
    enrollment = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'