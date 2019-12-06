from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  TipoIngrediente, Ingrediente, EstadoPedido, Pedido, DetallePedido, User

#HYPERLINKED
class AuthHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    class Meta:
        model = User
        fields = ['username', 'url']

class TipoIngredienteHySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoIngrediente
        fields = ['id','url','nombre']
    
class IngredienteHySerializer(serializers.HyperlinkedModelSerializer):
    tipo = TipoIngredienteHySerializer()
    class Meta:
        model = Ingrediente
        fields = ['id','url','nombre','tipo','precio','cantidad','imagen']


class EstadoPedidoHySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = ['id','url','nombre']

class PedidoHySerializer(serializers.HyperlinkedModelSerializer):
    estado = EstadoPedidoHySerializer()
    usuario = AuthHySerializers()
    class Meta:
        model = Pedido
        fields = ['id','url','cliente','fecha_pedido','monto_total','estado','usuario']

class DetallePedidoHySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['id','url','pedido','ingrediente','cantidad','precio']