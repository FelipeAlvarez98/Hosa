from django.contrib import admin
from .models import Dispositivosv1,Usuarios,Comunas,Regiones,Propiedades,Sectores,TipoSectores,TiposDispositivo,HorariosUso, UsuarioConfig, Planes, DetallesDispo, BitacoraSect, BitacoraDisp
# Register your models here.

admin.site.register(Regiones)
admin.site.register(Planes)
admin.site.register(Comunas)
admin.site.register(Usuarios)
admin.site.register(UsuarioConfig)
admin.site.register(TiposDispositivo)
admin.site.register(BitacoraDisp)
admin.site.register(DetallesDispo)
admin.site.register(Dispositivosv1)
admin.site.register(Propiedades)
admin.site.register(TipoSectores)
admin.site.register(BitacoraSect)
admin.site.register(HorariosUso)
admin.site.register(Sectores)