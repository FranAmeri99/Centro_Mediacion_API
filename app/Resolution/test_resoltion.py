from django.test import TestCase
from Resolution.models import Resolution
from django.utils.timezone import now

class CaseModelTest(TestCase):
    def test_create_resolution(self):
        """Create Resolution"""
        date = now()
        resolution = Resolution(date = date, description = 'description')

        self.assertEqual(resolution.description, 'description')
        self.assertEqual(resolution.date, date)
