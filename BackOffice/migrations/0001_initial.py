# Generated by Django 4.2.7 on 2023-11-27 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraDisp',
            fields=[
                ('idBitacoraDisp', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('fechaUso', models.DateField(verbose_name='Fecha de Uso')),
                ('horaUso', models.FloatField(verbose_name='Hora total de Uso')),
                ('gastoDiario', models.FloatField(verbose_name='Gasto Diário Energético')),
            ],
        ),
        migrations.CreateModel(
            name='BitacoraSect',
            fields=[
                ('idBitacoraSect', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('fechaUso', models.DateField(verbose_name='Fecha de Uso')),
                ('horaUso', models.FloatField(verbose_name='Hora total de Uso')),
                ('gastoDiario', models.FloatField(verbose_name='Gasto Diário Energético')),
            ],
        ),
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('idComuna', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreComuna', models.CharField(max_length=50, verbose_name='Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesDispo',
            fields=[
                ('idDetalleDispo', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('descripciondispo', models.CharField(max_length=50, verbose_name='Descripción del Dispositivo')),
                ('consumoHora', models.FloatField(verbose_name='Consumo Hora Dispositovo')),
                ('modeloDispo', models.CharField(max_length=50, verbose_name='Modelo del Dispositivo')),
                ('indicacionesDispo', models.CharField(max_length=50, verbose_name='Indicaciones del Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='HorariosUso',
            fields=[
                ('idHorarioUso', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreHoraUso', models.CharField(max_length=50, verbose_name='Nombre a Tiempo de Uso')),
                ('horaActivo', models.TimeField(verbose_name='Hora de Activación')),
                ('horaDesactivo', models.TimeField(verbose_name='Hora de Desactivación')),
                ('fechaActivo', models.DateField(verbose_name='Feha de Activación')),
                ('fechaDesactivo', models.DateField(verbose_name='Feha de Desactivación')),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('idPlan', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombrePlan', models.CharField(max_length=50, verbose_name='Nombre Plan')),
                ('descripcionPlan', models.CharField(max_length=50, verbose_name='Descripción del Plan')),
                ('cantidadDispositivos', models.IntegerField(verbose_name='Cantidad de Dispositivos')),
                ('precio', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedades',
            fields=[
                ('idPropiedad', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombrePropiedad', models.CharField(max_length=50, verbose_name='Nombre de la Propiedad')),
                ('direcUnicaPropiedad', models.CharField(max_length=50, verbose_name='Dirección Unica Propiedad')),
                ('direcUnica', models.CharField(max_length=50, verbose_name='Si tiene/No Tiene')),
            ],
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('idRegion', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreRegion', models.CharField(max_length=50, verbose_name='Región')),
            ],
        ),
        migrations.CreateModel(
            name='TiposDispositivo',
            fields=[
                ('idTipoDispositivo', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('tipoDispositivo', models.CharField(max_length=50, verbose_name='Tipo Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSectores',
            fields=[
                ('idSector', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('tipoSector', models.CharField(max_length=200, verbose_name='Tipo Sector')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioConfig',
            fields=[
                ('idConfigUsuario', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('detalleConfig', models.CharField(max_length=50, verbose_name='Detalle Config')),
                ('nombreConfig', models.CharField(max_length=50, verbose_name='Nombre de la configuracion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre Usuario')),
                ('rut', models.CharField(max_length=50, verbose_name='RUT')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo Electrónico')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('apodoUsuario', models.CharField(max_length=50, verbose_name='Apodo Usuario')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('idConfigUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.usuarioconfig', verbose_name='UsuarioConfig')),
                ('idPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.planes', verbose_name='PLAN')),
                ('idRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.regiones', verbose_name='REGIÓN')),
                ('idcomuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.comunas', verbose_name='COMUNA')),
            ],
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('idSector', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreSector', models.CharField(max_length=50, verbose_name='Nombre del Sector')),
                ('idBitacoraSect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.bitacorasect', verbose_name='Bitacora del Sector')),
                ('idPropiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.propiedades', verbose_name='PROPIEDAD')),
                ('idTipoSector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.tiposectores', verbose_name='TIPO SECTOR')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivosv1',
            fields=[
                ('idDispositivo', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('nombreDispositivo', models.CharField(max_length=50, verbose_name='Nombre Dispositivo')),
                ('consumoHora', models.FloatField(max_length=50, verbose_name='Ubicación del Dispositivo')),
                ('detallesUbicacion', models.CharField(max_length=50, verbose_name='Detalles para la Ubicación')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.usuarios', verbose_name='USUARIO')),
            ],
        ),
        migrations.AddField(
            model_name='comunas',
            name='idRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackOffice.regiones', verbose_name='REGIÓN'),
        ),
    ]
