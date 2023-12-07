from django.db import models

# Create your models here.
class Regiones(models.Model):
    idRegion = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreRegion = models.CharField(max_length=50, verbose_name="Región")

    def __str__(self):
        return self.nombreRegion
    
class Comunas(models.Model):
    idComuna = models.CharField(primary_key=True, unique=True,verbose_name="ID",max_length=30)
    nombreComuna = models.CharField(max_length=50, verbose_name="Comuna")
    idRegion = models.ForeignKey(Regiones,blank=False,on_delete=models.CASCADE,verbose_name="REGIÓN")
    
    def __str__(self):
        return self.nombreComuna
    
class Planes(models.Model):
    idPlan = models.CharField(primary_key=True, unique=True,verbose_name="ID",max_length=30)
    nombrePlan = models.CharField(verbose_name= "Nombre Plan", max_length=50)
    descripcionPlan = models.CharField(verbose_name= "Descripción del Plan", max_length=50)
    cantidadDispositivos = models.IntegerField(verbose_name="Cantidad de Dispositivos")
    precio = models.FloatField(verbose_name="Precio")
    
    def  __str__(self):
        return self.nombrePlan
    
class UsuarioConfig(models.Model):
    idConfigUsuario = models.CharField(primary_key=True, unique=True,verbose_name="ID",max_length=30)
    detalleConfig = models.CharField(verbose_name= "Detalle Config", max_length=50)
    nombreConfig = models.CharField(verbose_name= "Nombre de la configuracion", max_length=50)

    def  __str__(self):
        return self.detalleConfig

class Usuarios(models.Model):
    idUsuario = models.CharField(primary_key=True,unique=True,verbose_name="ID",max_length=30)
    nombreUsuario = models.CharField(verbose_name= "Nombre Usuario", max_length=50)
    rut = models.CharField(verbose_name="RUT", max_length=50)
    correo = models.EmailField(verbose_name= "Correo Electrónico",max_length=50)
    contraseña = models.CharField(verbose_name= "Contraseña", max_length=20)
    apodoUsuario = models.CharField(verbose_name= "Apodo Usuario", max_length=50)
    direccion = models.CharField(verbose_name= "Dirección", max_length=50)
    idcomuna = models.ForeignKey(Comunas, blank=False,on_delete=models.CASCADE,verbose_name="COMUNA")
    idRegion = models.ForeignKey(Regiones,blank=False,on_delete=models.CASCADE,verbose_name="REGIÓN")
    idPlan = models.ForeignKey(Planes, blank=False,on_delete=models.CASCADE,verbose_name="PLAN")
    idConfigUsuario = models.ForeignKey(UsuarioConfig, blank=False,on_delete=models.CASCADE,verbose_name="UsuarioConfig")

    def __str__(self):
        return self.nombreUsuario

class TiposDispositivo(models.Model):
    idTipoDispositivo = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    tipoDispositivo = models.CharField(max_length=50, verbose_name="Tipo Dispositivo")

    def __str__(self):
        return self.tipoDispositivo
    
class BitacoraDisp(models.Model):
    idBitacoraDisp = models.CharField(primary_key=True, unique=True, verbose_name="ID", max_length=30)
    fechaUso = models.DateField(verbose_name="Fecha de Uso")
    horaUso = models.FloatField(verbose_name="Hora total de Uso")
    gastoDiario = models.FloatField(verbose_name="Gasto Diário Energético")

    def __str__(self):
        return self.idBitacoraDisp
    
class DetallesDispo(models.Model):
    idDetalleDispo = models.CharField(primary_key=True, unique=True, verbose_name="ID", max_length=30)
    descripciondispo = models.CharField(verbose_name= "Descripción del Dispositivo", max_length=50)
    consumoHora = models.FloatField(verbose_name="Consumo Hora Dispositovo")
    modeloDispo = models.CharField(verbose_name= "Modelo del Dispositivo", max_length=50)
    indicacionesDispo = models.CharField(verbose_name= "Indicaciones del Dispositivo", max_length=50)
    
    def __str__(self):
        return self.descripciondispo

class Dispositivosv1(models.Model):
    idDispositivo = models.CharField(primary_key=True,unique=True,verbose_name="ID",max_length=30)
    nombreDispositivo = models.CharField(max_length=50, verbose_name="Nombre Dispositivo")
    consumoHora = models.FloatField(max_length=50, verbose_name="Ubicación del Dispositivo")
    detallesUbicacion = models.CharField(max_length=50, verbose_name="Detalles para la Ubicación")
    idUsuario = models.ForeignKey(Usuarios, blank=False,on_delete=models.CASCADE,verbose_name="USUARIO")

    def __str__(self):
        return self.nombreDispositivo
    
class Propiedades(models.Model):
    idPropiedad = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombrePropiedad = models.CharField(max_length=50, verbose_name="Nombre de la Propiedad")
    direcUnicaPropiedad = models.CharField(max_length=50, verbose_name="Dirección Unica Propiedad")
    direcUnica = models.CharField(max_length=50, verbose_name="Si tiene/No Tiene")

    def __str__(self):
        return self.nombrePropiedad

class TipoSectores(models.Model):
    idSector = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    tipoSector = models.CharField(max_length=200, verbose_name="Tipo Sector")

    def __str__(self):
        return self.tipoSector
    
class BitacoraSect(models.Model):
    idBitacoraSect = models.CharField(primary_key=True, unique=True, verbose_name="ID", max_length=30)
    fechaUso = models.DateField(verbose_name="Fecha de Uso")
    horaUso = models.FloatField(verbose_name="Hora total de Uso")
    gastoDiario = models.FloatField(verbose_name="Gasto Diário Energético")

    def __str__(self):
        return self.idBitacoraSect

class HorariosUso(models.Model):
    idHorarioUso = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreHoraUso = models.CharField(max_length=50, verbose_name="Nombre a Tiempo de Uso")
    horaActivo = models.TimeField(verbose_name="Hora de Activación")
    horaDesactivo = models.TimeField(verbose_name="Hora de Desactivación")
    fechaActivo = models.DateField(verbose_name="Feha de Activación")
    fechaDesactivo = models.DateField(verbose_name="Feha de Desactivación")

    def __str__(self):
        return self.idHorarioUso

class Sectores(models.Model):
    idSector = models.CharField(primary_key=True, unique=True, verbose_name="ID",max_length=30)
    nombreSector = models.CharField(max_length=50, verbose_name="Nombre del Sector")
    idTipoSector = models.ForeignKey(TipoSectores, blank=False, on_delete=models.CASCADE, verbose_name="TIPO SECTOR")
    idBitacoraSect = models.ForeignKey(BitacoraSect, blank=False, on_delete=models.CASCADE, verbose_name="Bitacora del Sector")
    idPropiedad = models.ForeignKey(Propiedades, blank=False, on_delete=models.CASCADE, verbose_name="PROPIEDAD")

    def __str__(self):
        return self.nombreSector