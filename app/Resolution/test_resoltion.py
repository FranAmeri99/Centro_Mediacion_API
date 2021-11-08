from django.test import TestCase
from Resolution.models import Resolution
    
class CaseModelTest(TestCase):
    def test_create_resolution(self):
        """Create Resolution"""
        resolution = Resolution(date = '08/11/2021', description = 'description')

        self.assertEqual(resolution.description, 'description')
        self.assertEqual(resolution.date, '08/11/2021')
