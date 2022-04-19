from django.urls import path
from django.views.generic import TemplateView
from entrega_intermedia.forms.views import Vueloview, Pasajeroview, Tripulacionview

app_name = "formulario"
urlpatterns = [
    # path("", TemplateView.as_view(template_name="v2/index.html"), name="v2"),
    # path("aboutus/", TemplateView.as_view(template_name="v2/aboutus.html"), name="about-us"),
    
    # path("template/", TemplateView.as_view(template_name="v2/home.html"), name="v2"),
    # path("diigo", TemplateView.as_view(template_name="diigo/index.html"), name="diigo"),
    # path("student/", Studentview.as_view(), name="studentv2"),

    # path("formularios/", FormularioView.as_view(), name="formulario"),
    # path("search/", SearchView.as_view(), name="search"),
    path("vuelo/", Vueloview.as_view(), name="vuelo"),
    path("pasajero/", Pasajeroview.as_view(), name="pasajero"),
    path("tripulacion/", Tripulacionview.as_view(), name="tripulacion"),
]