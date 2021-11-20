from rest_framework import serializers
from users.models import User

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','name', 'last_name' ,'email', 'password')
        #fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self,instance,validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user



class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id:': instance['id'],
            'password': instance['password'],
            'is_superuser': instance['is_superuser'],
            'enrollment': instance['enrollment'],
            'dni': instance['dni'],
            'username': instance['username'],
            'email': instance['email'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'is_staff': instance['is_staff']
        }
