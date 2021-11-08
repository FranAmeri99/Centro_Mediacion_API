from django.db import models

class Resolution(models.Model):
    date        = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def create_resolution(self, date, description):
        resolution = self.model(date,description)
        resolution.save(using=self._db)
        return resolution

    def __str__(self):
        return self.description
