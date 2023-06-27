import numpy 
import estudioxd as fn
import time

acumulador=0
contador=0
lista_rut=[]
lista_nombres=[]
lista_nombre_mascota=[]
lista_cant=[]



habitaciones = numpy.zeros((2,5),int)

while True:
    print(""" MENÚ MASCOTA SEGURA
    1.Grabar.(guardar datos de la mascota.)
    2.Buscar.
    3.Retirarse.
    4. salir.

    """)

    opcion=fn.validar_opcion()
    if opcion == 1:
        rut=fn.validar_rut()
        lista_rut.append(rut)
        nombre=fn.validar_nombre()
        lista_nombres.append(nombre)        
        id= acumulador =+1
        nombre_mascota=fn.validar_nombre_mascota()
        lista_nombre_mascota.append(nombre_mascota)
        cant=fn.validar_cantidad()
        lista_cant.append(cant)

        for x in range (2):
            print(f"habitacion {(x+1)*2}", end=" ")
            for y in range(5):
                print(habitaciones [x][y], end=" ")

    elif opcion==2:
        if fn.validar_rut in (lista_rut):
            print()

    elif opcion ==3:
        rut=fn.validar_rut()
        if rut in (lista_rut):
            print(f"El total a pagar es:{cant*15000}.")
            time.sleep(3)

    else:
        print("Gracias por su preferencia!!")
        break                


