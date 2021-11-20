from rest_framework import serializers

from Resolution.models import *

class ResolutionPortfolioSerializers(serializers.ModelSerializer):
    class Meta:
        model = ResolutionPortfolio
        fields = '__all__'
class ResolutionSessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ResolutionSession
        fields = '__all__'
