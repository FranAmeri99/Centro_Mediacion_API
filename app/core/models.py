from django.db import models

from Users.models import *
from Resolution.models import Resolution

from django.utils.timezone import now

class State(models.Model):
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.description

class Case(models.Model):
    mediator         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mediator')
    lawyer_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_applicant')
    client_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_applicant')
    lawyer_defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_defendant')
    client_defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_defendant')
    name             = models.CharField(max_length=255)
    def __str__(self):
        return "%s --- %s --- %s" % (self.id, self.name, self.mediator.email)

class MediationPortafolio(models.Model):
    start_date = models.DateField(default=now())
    end_date   = models.DateField(default=now())
    state      = models.ForeignKey(State, on_delete=models.CASCADE)
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    case       = models.ForeignKey(Case, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.case.name, self.start_date)

class MediationSessions(models.Model):
    mediatonPortafolio = models.ForeignKey(MediationPortafolio, on_delete=models.CASCADE, related_name = 'mediatonPortafolio')
    resolution         = models.ForeignKey(Resolution, on_delete=models.CASCADE, related_name = 'resolution')
    
    def __str__(self):
        return "%s" % (self.mediatonPortafolio.name)

