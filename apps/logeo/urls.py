from django.urls import path, include
from rest_framework import routers
#from .views import AuthApiList, RolApiList, UsuarioApiList
#from .viewsets import AuthViewSets, RolViewSets, UsuarioViewSets
from .viewsets import RolHypViewSet, AuthHypViewSet, UsuarioHypViewSet

router = routers.DefaultRouter()

#HYPERLINKEDSERIALIZER - viewsets
router.register(r'rol', RolHypViewSet)
router.register(r'auth', AuthHypViewSet)
router.register(r'usuario', UsuarioHypViewSet)

urlpatterns = [
    path('logeo/', include(router.urls))
]
