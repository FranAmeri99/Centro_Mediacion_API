from django.db import models

from users.models import *
from Resolution.models import *

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
    case       = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.case.name, self.start_date)

class MediationSessions(models.Model):
    portfolio = models.ForeignKey(MediationPortafolio, on_delete=models.CASCADE, related_name = 'portfolio')
    date = models.DateField(default=now())
    
    def __str__(self):
        return "%s %s" % (self.portfolio.case.name, self.date)
    