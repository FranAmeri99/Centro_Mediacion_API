from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.utils import timezone
import datetime
from django.utils.timezone import now

class UserManager(BaseUserManager):

    def _create_user(self, username, email, name, last_name, dni,  password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            dni = dni,
            enrollment = dni,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def _create_luser(self, username, email, name, last_name, dni, enrollment ,password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            dni = dni,
            enrollment = enrollment,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name,dni, password=None, **extra_fields):
        """Cretats and saves a new user"""
        if not email:
            raise ValueError("users must have an email addres")
        user = self._create_user(username,self.normalize_email(email), name, last_name, dni, password, False, False, **extra_fields)
        user.set_password(password)
        return user


    def create_superuser(self, username, email, name, last_name, dni, enrollment, password=None, **extra_fields):
        """Cretats and saves a new super user"""
        superuser = self._create_luser(username,self.normalize_email(email), name, last_name, dni,enrollment ,password, True, True, **extra_fields)
        superuser.enrollment = enrollment
        return superuser

    def create_lawyer(self, username, email, name, last_name, dni, enrollment,   password=None, **extra_fields):
        """Cretats and saves a new lawyer"""
        lawyer = self._create_luser(username,self.normalize_email(email), name, last_name,dni, password, False, False, **extra_fields)
        lawyer.enrollment = enrollment
        return lawyer

    def create_mediator(self, username, email, name, last_name, dni, enrollment,   password=None, **extra_fields):
        """Create and saves new lawyer user"""
        mediator = self._create_luser(username,self.normalize_email(email), name, last_name,dni, password, True, True, **extra_fields)
        mediator.enrollment = enrollment
        return mediator

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email insted of username"""
    enrollment = models.CharField("Enrollment:",blank = True, unique = True,max_length=255)#, unique=True)
    dni = models.CharField("Dni:",max_length=255)#, unique=True)
    username = models.CharField('UserName:', unique = True,max_length = 255)
    email = models.EmailField('Email:',max_length = 255)#, unique = True)
    name = models.CharField('Name', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Last_name', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name', 'dni', 'enrollment']

    def __str__(self):
        return f'{self.name} {self.last_name}'
