from multiprocessing import context
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import VueloForms, PasajeroForms, TripulacionForms
from entrega_intermedia.mvt.models import Vuelo, Pasajero, Tripulacion

class Vueloview(TemplateView):
   
   template_name = 'forms/formulario_vuelo.html'
    

   def get(self, request):
      context = {
         'form' : VueloForms()
      }
      return render(request, self.template_name, context)

   def post(self, request):
        
      response = VueloForms(request.POST)

      print(response)

      if response.is_valid:
         obj_response = response.cleaned_data

         obj_vuelo = Vuelo(
                        airline = obj_response.get('airline'),
                        number = obj_response.get('number')
                           )
         obj_vuelo.save()

         context = {
            'form' : VueloForms()
            }
      return render(request ,self.template_name, context)

class Pasajeroview(TemplateView):
   
   template_name = 'forms/formulario_pasajero.html'
    
   def get(self, request):
      context = {
            'form' : PasajeroForms()
      }
      return render(request, self.template_name, context)

   def post(self, request):
        
      response = PasajeroForms(request.POST)

      print(response)

      if response.is_valid:

         obj_response = response.cleaned_data

         obj_pasajero = Pasajero(
                        name = obj_response.get('name'),
                        lastname = obj_response.get('lastname'),
                        email = obj_response.get('email')
                           )
         obj_pasajero.save()

         context = {
            'form' : PasajeroForms()
         }
      
      return render(request ,self.template_name, context)

class Tripulacionview(TemplateView):
   
   template_name = 'forms/formulario_tripulacion.html'
    

   def get(self, request):
      context = {
         'form' : TripulacionForms()
      }
      return render(request, self.template_name, context)

   def post(self, request):
      response = TripulacionForms(request.POST)

      print(response)

      if response.is_valid:
         
         obj_response = response.cleaned_data

         obj_curso = Tripulacion(
                                 name = obj_response.get('name'),
                                 lastname = obj_response.get('lastname'),
                                 worked = obj_response.get('worked')
                                 )
         obj_curso.save()

         context = {
            'form' : TripulacionForms()
         }
        
      return render(request ,self.template_name, context)

class SearchPasajero(TemplateView):
   
   template_name = 'forms/search_pasajero.html'

   def post(self, request):

      context = {
         "elements" : Pasajero.objects.filter(
               name__icontains=request.POST.get('name')
               )
      }

      return render(request, self.template_name, context)

class SearchVuelo(TemplateView):
   
   template_name = 'forms/search_vuelo.html'

   def post(self, request):

      context = {
         "elements" : Vuelo.objects.filter(
               number__icontains=request.POST.get('number')
               )
      }

      return render(request, self.template_name, context)

class SearchTripulacion(TemplateView):
   
   template_name = 'forms/search_tripulacion.html'

   def post(self, request):

      context = {
         "elements" : Tripulacion.objects.filter(
               worked__icontains=request.POST.get('worked')
               )
      }

      return render(request, self.template_name, context)