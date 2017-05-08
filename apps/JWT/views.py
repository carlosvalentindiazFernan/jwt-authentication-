
from django.shortcuts import render
from .serializer import UserSerializer,CarSerializer,CarUserSerializer
from rest_framework import generics
from apps.cars.models import Car,CarUser
from django.contrib.auth.models import User
from .pagination import LargePaginationCar
from django.views.generic.base import TemplateView


class CarView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ListCarros(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = LargePaginationCar




class CarUserView(generics.CreateAPIView):
    queryset = CarUser.objects.all()
    serializer_class = CarUserSerializer



class CarUserList(generics.ListAPIView):
    queryset = CarUser.objects.all()
    serializer_class = CarUserSerializer
    pagination_class = LargePaginationCar

