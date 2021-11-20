from rest_framework import serializers

from core.models import *

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        #fields = ['name']


class CaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['name']
        #        fields = ['username', 'name', 'last_name',]

class PortafolioSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediationPortafolio
        fields = '__all__'
        #        fields = ['username', 'name', 'last_name',]


class SessionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediationSessions
        fields = '__all__'
        #        fields = ['username', 'name', 'last_name',]
