from django.test import TestCase
from django.contrib.auth import get_user_model
from Users.models import *
class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email"""
        email = 'test@francisco.com'
        password = 'Password99?'
        user = get_user_model().objects.create_user(
        email=email, 
        password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_creat_new_superuser(self):
        """"Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@superuser.com', 
            'test123'
            )
            
        self.assertTrue(user.is_staff)
        

    def test_creat_new_mediator(self):
        """"Test creating a new mediator"""

        user = get_user_model().objects.create_mediator(
            'test@superuser.com', 
            'test123',
            '1111'
            )
            
        self.assertTrue(user.is_staff)
        
    def test_create_user_all_data(self):
        """Test creating a user complet"""
        email = 'test@francisco.com'
        password = 'Password99?'
        name = 'francisco'
        last_name = 'Ameri'
        gender = 'male'
        dni = 11111111
        nationality = 'Argentino'
        birth_date = '18/02/1999'
        username = 'FranAmeri'
        enrollment = '1111'

        user = get_user_model().objects.create_user(
        email=email, 
        password=password,
        name=name,
        last_name=last_name,
        gender=gender,
        dni=dni,
        nationality =nationality,
        birth_date=birth_date,
        username=username,
        enrollment=enrollment
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.gender, gender)
        self.assertEqual(user.dni, dni)
        self.assertEqual(user.nationality, nationality)
        self.assertEqual(user.username, username)
        self.assertEqual(user.enrollment, enrollment)
        self.assertTrue(user.check_password(password))

    def test_create_lawyer_user(self):
        """Test creating a Lawyer"""
        email = 'test@superuser.com'
        password = 'test123'
        enrollment = '11111111111212'
        user = get_user_model().objects.create_lawyer_user(
            email = email,
            password = password,
            enrollment = enrollment,
            )
        
        self.assertEqual(user.enrollment, enrollment)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_user_email(self):
        """Test User Email"""
        email = 'test@FRANCISCO.com'
        user =get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):

        """Test creating user no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
