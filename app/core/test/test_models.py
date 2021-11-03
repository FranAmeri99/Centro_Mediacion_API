from django.test import TestCase
from django.contrib.auth import get_user_model

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

    def test_user_email(self):
        email = 'test@FRANCISCO.com'
        user =get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        #"Test creating user no email raises error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_creat_new_superuser(self):
        """"Test creating a new superuser"""

        user = get_user_model().objects.creat_super_user(
            'test@superuser.com', 
            'test123'
            )
            
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)