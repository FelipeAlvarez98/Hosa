from rest_framework import viewsets
from .serializer import RegionesSerializer, PlanesSerializer, ComunasSerializer, UsuariosSerializer, TiposDispositivoSerializer, BitacoraDispSerializer, DetallesDispoSerializer,Dispositivosv1Serializer, PropiedadesSerializer, TipoSectoresSerializer, BitacoraSectSerializer, HorariosUsoSerializer, SectoresSerializer , UsuarioConfigSerializer
from .models import Regiones, Planes, Comunas, Usuarios, TiposDispositivo, BitacoraDisp, DetallesDispo, Dispositivosv1, Propiedades, TipoSectores, BitacoraSect, HorariosUso, Sectores, UsuarioConfig


class RegionesViewSet(viewsets.ModelViewSet):
    queryset=Regiones.objects.all()
    serializer_class = RegionesSerializer

class PlanesViewSet(viewsets.ModelViewSet):
    queryset=Planes.objects.all()
    serializer_class = PlanesSerializer

class ComunasViewSet(viewsets.ModelViewSet):
    queryset=Comunas.objects.all()
    serializer_class = ComunasSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class UsuarioConfigViewSet(viewsets.ModelViewSet):
    queryset=UsuarioConfig.objects.all()
    serializer_class = UsuarioConfigSerializer

class TiposDispositivoViewSet(viewsets.ModelViewSet):
    queryset=TiposDispositivo.objects.all()
    serializer_class = TiposDispositivoSerializer

class BitacoraDispViewSet(viewsets.ModelViewSet):
    queryset=BitacoraDisp.objects.all()
    serializer_class = BitacoraDispSerializer

class DetallesDispoViewSet(viewsets.ModelViewSet):
    queryset=DetallesDispo.objects.all()
    serializer_class = DetallesDispoSerializer

class Dispositivosv1ViewSet(viewsets.ModelViewSet):
    queryset=Dispositivosv1.objects.all()
    serializer_class = Dispositivosv1Serializer

class PropiedadesViewSet(viewsets.ModelViewSet):
    queryset=Propiedades.objects.all()
    serializer_class = PropiedadesSerializer

class TipoSectoresViewSet(viewsets.ModelViewSet):
    queryset=TipoSectores.objects.all()
    serializer_class = TipoSectoresSerializer

class BitacoraSectViewSet(viewsets.ModelViewSet):
    queryset=BitacoraSect.objects.all()
    serializer_class = BitacoraSectSerializer

class HorariosUsoViewSet(viewsets.ModelViewSet):
    queryset=HorariosUso.objects.all()
    serializer_class = HorariosUsoSerializer

class SectoresViewSet(viewsets.ModelViewSet):
    queryset=Sectores.objects.all()
    serializer_class = SectoresSerializer