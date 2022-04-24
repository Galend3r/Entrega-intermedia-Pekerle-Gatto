from django.urls import path
from entrega_intermedia.forms.views import Vueloview, Pasajeroview, Tripulacionview, SearchPasajero, SearchVuelo, SearchTripulacion

app_name = "formulario"
urlpatterns = [
    path("vuelo/", Vueloview.as_view(), name="vuelo"),
    path("pasajero/", Pasajeroview.as_view(), name="pasajero"),
    path("tripulacion/", Tripulacionview.as_view(), name="tripulacion"),

    path("search_pasajero/", SearchPasajero.as_view(), name="search-pasajero"),
    path("search_vuelo/", SearchVuelo.as_view(), name="search-vuelo"),
    path("search_tripulacion/", SearchTripulacion.as_view(), name="search-tripulacion"),
]