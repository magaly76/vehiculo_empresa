from .models import Vehiculo, Chofer, RegistroContabilidad
from datetime import date

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo(
        patente = patente,
        marca = marca,
        modelo = modelo,
        year = year
    )

    vehiculo.save()
    return vehiculo

def crear_chofer(rut, nombre, apellido, patente):
    if not rut.isdigit():
        print('Ingresar RUT sin punto ni guión.')
        return
        
    vehiculo = Vehiculo.objects.get(patente=patente)
    
    chofer = Chofer(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
        activo = False,
        creacion_registro = date.today(),
        patente = vehiculo
    )

    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra, valor, patente):
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        registro_contabilidad = RegistroContabilidad(
            fecha_compra = fecha_compra,
            valor=valor,
            patente=vehiculo  # Asigna la instancia del vehículo
        )

        registro_contabilidad.save()
        print("Registro contable creado exitosamente")

    except Vehiculo.DoesNotExist:
        print(f"No se encontró un vehículo con la patente {patente}")

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    print(f'Chofer con RUT {rut} ha sido deshabilitado.')

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()
    print(f'El chofer con rut {rut} ha sido habilitado.')

def deshabilitar_vehiculo():
    print('funcion no habilitada')

def habilitar_vehiculo():
    print('funcion no habilitada')

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return (f'Patente:{vehiculo.patente} Marca:{vehiculo.marca} Modelo:{vehiculo.modelo} Año:{vehiculo.year}')
    

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return (f'Chofer:{chofer.rut} Nombre:{chofer.nombre} Apellido:{chofer.apellido} Vehiculo Asignado:{chofer.patente}')
    
def asignar_chofer_a_vehiculo(rut_chofer, patente_vehiculo):
    chofer = Chofer.objects.get(rut=rut_chofer)
    vehiculo = Vehiculo.objects.get(patente=patente_vehiculo)
    chofer.patente = vehiculo
    chofer.save()
    print(f'El chofer con el rut {rut_chofer} ha sido asignado al vehiculo con patente {patente_vehiculo}.')
    
def imprimir_datos_vehiculo():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f'Patente:{vehiculo.patente} Marca:{vehiculo.marca} Modelo:{vehiculo.modelo} Año:{vehiculo.year}' )
