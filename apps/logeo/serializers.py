from rest_framework import serializers
from .models import Usuario, Rol, User
from django.contrib.auth.models import User

#HIPERLINKEDSERIALIZERS

class RolHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='Rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True)
    class Meta:
        model = Rol
        fields = ['id','url','rol']

class AuthHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='User-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    url = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, lookup_field='username')
    class Meta:
        model = User
        fields = ['id','password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined', 'url']

class UsuarioHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='Usuario-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='Usuario-detail')
    url = serializers.HyperlinkedRelatedField(view_name='usuario-detail', read_only=True, lookup_field='rol')
    #rol = RolHySerializers(many=True, read_only=True)
    #rol = AuthHySerializers(many=True, read_only=True)
    rol = RolHySerializers()
    user = AuthHySerializers()
    class Meta:
        model = Usuario
        fields = ['id','user','rol','location','age','url']