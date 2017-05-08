from rest_framework import mixins
from rest_framework import generics

from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [

    url(r'^car/$', CarView.as_view(),name='CarCRUD'),
    url(r'^carlist/$', ListCarros.as_view(), name='CarList'),


    url(r'^userlist/$', UserList.as_view(),name='UserList'),


    url(r'^car-uses/$', CarUserView.as_view(),name='CarUsesCRUD'),
    url(r'^car-uses-list/$', CarUserList.as_view(),name='CarUsesCRUD'),


]
urlpatterns = format_suffix_patterns(urlpatterns)