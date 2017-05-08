from rest_framework import mixins
from rest_framework import generics

from django.conf.urls import url,include
from .views import *

urlpatterns = [

    url(r'^car-edit/$', CarCRUD.as_view(),name='CarCRUDEdit')

]
