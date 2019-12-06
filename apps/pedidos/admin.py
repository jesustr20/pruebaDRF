from django.contrib import admin
from .models import TipoIngrediente, Ingrediente ,EstadoPedido, Pedido, DetallePedido
# Register your models here.

class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'tipo', 'precio', 'cantidad']

class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','cliente', 'fecha_pedido', 'monto_total', 'estado', 'usuario']

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido', 'ingrediente', 'cantidad', 'precio']

admin.site.register(TipoIngrediente, TipoIngredienteAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(EstadoPedido, EstadoPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)