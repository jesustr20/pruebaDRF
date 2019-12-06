from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TipoIngrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null = True, blank=True)

    def __str__(self):
        return f'{str(self.nombre)}'

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null = True , blank=True)
    tipo = models.ForeignKey (TipoIngrediente,on_delete= models.CASCADE)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to="pictures/%y", null=True)

    def __str__(self):
        return f'{str(self.nombre)}'

class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null = True, blank=True)

    def __str__(self):
        return (self.nombre)

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=255, null = True, blank = True)
    fecha_pedido = models.DateTimeField()
    monto_total = models.DecimalField(max_digits=16, decimal_places=2)
    estado = models.ForeignKey(EstadoPedido, on_delete = models.CASCADE)
    usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return f'{str(self.id)}'

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return f'{str(self.ingrediente)}'