from django.views.generic import ListView
from cobro.tarjeta.models import Rtarjeta


class RtarjetaListView(ListView):
    model= Rtarjeta
    template_name = 'index.html'

