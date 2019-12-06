from rest_framework import serializers
from .models import Usuario, Rol, User
from django.contrib.auth.models import User

#HIPERLINKEDSERIALIZERS
class AuthHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    class Meta:
        model = User
        fields = ['id','password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined', 'url']

class RolHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    class Meta:
        model = Rol
        fields = ['id','url','rol']

class UsuarioHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    #rol = RolHySerializers(many=True, read_only=True)
    rol = RolHySerializers()
    user = AuthHySerializers()
    class Meta:
        model = Usuario
        fields = ['id','user','rol','location','age','url']