from django.contrib import admin
from .models import Usuario, Rol
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'age', 'rol', 'location']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id','rol']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol, RolAdmin)