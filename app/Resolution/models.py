from django.db import models
from django.utils.timezone import now
class Resolution(models.Model):
    date        = models.DateField(default=now())
    description = models.CharField(max_length=255)

    def create_resolution(self, date, description):
        resolution = self.model(date,description)
        resolution.save(using=self._db)
        return resolution

    def __str__(self):
        return self.description
