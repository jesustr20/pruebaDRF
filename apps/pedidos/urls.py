from django.urls import path, include
#from .viewsets import TipoIngredienteViewSet, IngredienteViewSet, RolViewSet, EstadoPedidoViewSet, PedidoViewSet, DetallePedidoViewSet
from rest_framework import routers
from .viewsets import TipoIngredienteHypViewSet, IngredienteHypViewSet, EstadoPedidoHypViewSet, PedidoHypViewSet, DetallePedidoHypViewSet

router = routers.DefaultRouter()

router.register(r'TipoIngredientes', TipoIngredienteHypViewSet)
router.register(r'Ingredientes', IngredienteHypViewSet)
router.register(r'EstadoPedidos', EstadoPedidoHypViewSet)
router.register(r'Pedidos', PedidoHypViewSet)
router.register(r'DetallePedidos', DetallePedidoHypViewSet)

urlpatterns = [
    path('pedido/', include (router.urls))
]