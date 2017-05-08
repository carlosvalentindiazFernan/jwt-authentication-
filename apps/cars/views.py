from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Car
from .forms import CarForm
# Create your views here.



class Home(TemplateView):
    template_name = 'index.html'



class CarCRUD(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'index.html'
    success_url = '/'
