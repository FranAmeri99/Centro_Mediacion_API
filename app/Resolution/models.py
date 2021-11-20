from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from core.models import MediationSessions, MediationPortafolio

class ResolutionPortfolio(models.Model):
    date        = models.DateField(default=now())
    description = models.CharField(max_length=255)
    portfolio = models.ForeignKey(MediationPortafolio, on_delete=models.CASCADE, related_name='portofolio')
    def create_resolution_portfolio(self, date, description, portfolio):
        resolution_portfolio = self.model(date,description, portfolio)
        resolution_portfolio.save(using=self._db)
        return resolution_portfolio

    def __str__(self):
        return self.portfolio.case.name

class ResolutionSession(models.Model):
    date        = models.DateField(default=now())
    description = models.CharField(max_length=255)
    session = models.ForeignKey(MediationSessions, on_delete=models.CASCADE, related_name='session')
    """
    def create_resolution_session(self, date, description, session):
        resolution_session = self.model(date,description, session)
        resolution_session.save(using=self._db)
        return resolution_session
    """
    def __str__(self):
        return "%s /Informe: %s" % (self.session.portfolio.case.name,self.description )
