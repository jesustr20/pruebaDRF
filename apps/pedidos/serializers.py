from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  TipoIngrediente, Ingrediente, EstadoPedido, Pedido, DetallePedido, User

#HYPERLINKED
class AuthHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    url = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = User
        fields = ['username', 'url']

class TipoIngredienteHySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoIngrediente
        fields = ['id','url','nombre']
    
class IngredienteHySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name='tipoingrediente-detail', read_only=True)
    tipo = TipoIngredienteHySerializer()
    class Meta:
        model = Ingrediente
        fields = ['id','url','nombre','tipo','precio','cantidad','imagen']


class EstadoPedidoHySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name='estado-detail', read_only=True)
    class Meta:
        model = EstadoPedido
        fields = ['id','url','nombre']

class PedidoHySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name='estado-detail', read_only=True)
    estado = EstadoPedidoHySerializer()
    usuario = AuthHySerializers()
    class Meta:
        model = Pedido
        fields = ['id','url','cliente','fecha_pedido','monto_total','estado','usuario']

class DetallePedidoHySerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedRelatedField(view_name='pedido-detail', read_only=True)
    ingrediente = IngredienteHySerializer()
    pedido = PedidoHySerializer()
    class Meta:
        model = DetallePedido
        fields = ['id','url','pedido','ingrediente','cantidad','precio']