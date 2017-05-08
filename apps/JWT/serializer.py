from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.cars.models import Car,CarUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User = get_user_model()
        fields=(
            'id', 'username','email'
        )



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=(
            'id','name'
        )



class CarUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=CarUser
        fields=(
            'id','userid','carid'
        )