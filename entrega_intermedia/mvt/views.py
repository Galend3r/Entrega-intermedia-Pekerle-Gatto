from multiprocessing import context
from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render

class Homeview(TemplateView):

     template_name = 'ocean/index.html'
    

     def get(self, request):
        return render(request, self.template_name)