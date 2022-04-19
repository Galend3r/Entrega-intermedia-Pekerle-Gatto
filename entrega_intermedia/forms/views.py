from multiprocessing import context
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render

class Vueloview(TemplateView):

     template_name = 'forms/formulario_vuelo.html'
    

     def get(self, request):
        return render(request, self.template_name)

class Pasajeroview(TemplateView):

     template_name = 'forms/formulario_pasajero.html'
    

     def get(self, request):
        return render(request, self.template_name)

class Tripulacionview(TemplateView):

     template_name = 'forms/formulario_tripulacion.html'
    

     def get(self, request):
        return render(request, self.template_name)