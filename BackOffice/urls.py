from django.urls import include, path 
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from BackOffice import views

# api version 
router=routers.DefaultRouter()
router.register(r'regiones', views.RegionesViewSet)
router.register(r'planes', views.PlanesViewSet)
router.register(r'comunas', views.ComunasViewSet)
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'usuarioConfig', views.UsuarioConfigViewSet)
router.register(r'tipoDispositivos', views.TiposDispositivoViewSet)
router.register(r'bitacoraDisp', views.BitacoraDispViewSet)
router.register(r'detallesDispo', views.DetallesDispoViewSet)
router.register(r'Dispositivosv1', views.Dispositivosv1ViewSet)
router.register(r'propiedades', views.PropiedadesViewSet)
router.register(r'tipoSectores', views.TipoSectoresViewSet)
router.register(r'bitacoraSect', views.BitacoraSectViewSet)
router.register(r'horariosUso', views.HorariosUsoViewSet)
router.register(r'sectores', views.SectoresViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="BackOffice API") )
]
