from rest_framework import serializers
from .models import Regiones, Planes, Comunas, Usuarios, TiposDispositivo, BitacoraDisp, DetallesDispo, Dispositivosv1, Propiedades, TipoSectores, BitacoraSect, HorariosUso, Sectores,UsuarioConfig

class RegionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiones
        fields='__all__'

class ComunasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunas
        fields='__all__'

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields='__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields='__all__'
        
class UsuarioConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioConfig
        fields='__all__'

class TiposDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDispositivo
        fields='__all__'

class BitacoraDispSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitacoraDisp
        fields='__all__'

class DetallesDispoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesDispo
        fields='__all__'

class Dispositivosv1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivosv1
        fields='__all__'

class PropiedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedades
        fields='__all__'

class TipoSectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSectores
        fields='__all__'

class BitacoraSectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitacoraSect
        fields='__all__'

class HorariosUsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorariosUso
        fields='__all__'

class SectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectores
        fields='__all__'