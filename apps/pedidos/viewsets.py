from rest_framework import viewsets
from django.contrib.auth.models import User
#from .serializers import TipoIngredienteSerializer,IngredienteSerializer,  RolSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer
from .models import TipoIngrediente, Ingrediente, EstadoPedido,Pedido, DetallePedido, User
from .serializers import TipoIngredienteHySerializer, IngredienteHySerializer, EstadoPedidoHySerializer, PedidoHySerializer, DetallePedidoHySerializer, AuthHySerializers

#HYPERLINKED

class AuthHypViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthHySerializers

class TipoIngredienteHypViewSet(viewsets.ModelViewSet):
    queryset = TipoIngrediente.objects.all()
    serializer_class = TipoIngredienteHySerializer

class IngredienteHypViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteHySerializer

class EstadoPedidoHypViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoHySerializer

class PedidoHypViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoHySerializer

class DetallePedidoHypViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoHySerializer