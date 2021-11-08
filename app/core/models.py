from django.db import models

from Users.models import *
#from Resolution.models import Resolution  AGUS DESARROLLAR


class State(models.Model):
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.description

class Case(models.Model):
    meditor = models.ForeignKey(User, on_delete=models.CASCADE)
    lawyer_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_applicant')
    client_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_applicant')
    lawyer_defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_defendant')
    client_defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_defendant')
    
class MediationPortafolio(models.Model):
    name       = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date   = models.CharField(max_length=255)
    state      = models.ForeignKey(State, on_delete=models.CASCADE)
    #resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)   AGUS DESARROLLAR
    case       = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.start_date)

class MediationSessions(models.Model):
    mediatonPortafolio = models.ForeignKey(MediationPortafolio, on_delete=models.CASCADE)
    #resolution         = models.ForeignKey(Resolution, on_delete=models.CASCADE)   AGUS DESARROLLAR
    
    def __str__(self):
        return "%s %s %s" % (self.mediatonPortafolio.name, self.resolution.name)

