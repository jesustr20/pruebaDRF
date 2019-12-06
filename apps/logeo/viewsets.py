from rest_framework import viewsets, filters, permissions
from .models import Usuario, User, Rol
from django.contrib.auth.models import User
#from .serializers import UsuarioSerializers, AuthSerializers, RolSerializers
from .serializers import RolHySerializers, AuthHySerializers, UsuarioHySerializers

#HyperlinkedModelSerializers
class RolHypViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolHySerializers

class AuthHypViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthHySerializers

class UsuarioHypViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioHySerializers