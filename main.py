from hospital import *
from farmacia import *
import pickle
import os

def main():
    while True:
        try:
            os.system('cls')
            print('HOSPITAL UDENAR')
            print('---------------------------------')
            print('   1. Manejo medicos')
            print('   2. Manejo pacientes ')
            print('   3. Manejar Farmacia ')
            print('   4. Manejar pedidos ')
            print('')
            print('   5. SALIR')
            print('--------------------------------')
            opcion =int(input('Elija una opción: '))
            match opcion:
                case 1:
                    pass
                case 2:
                    pass 
                case 3:
                    menu_farmacia()
                case 4:
                    
                    os.system('pause')
                case 5:
                    print('Gracias por usar nuestro sistema ')
                    break
                case other: 
                    print('Ha digitado una opción invalida ')
                    os.system("pause")
        except ValueError:
            print('Digitacion incorrecta, intentelo de nuevo')

# SE INICIA LA CREACION DE LA FARMACIA
farmacia_creada=False
def crear_farmacia():
    global farmacia_creada
    farmacia=FARMACIA([],[])
    farmacia.registrar_producto()
    with open("farmacia.pickle","wb") as f:
        pickle.dump(farmacia,f)
    return farmacia
    #SE REGISTRA UN PRODUCTO EN LA FARMACIA

def menu_farmacia():
    global farmacia_creada
    os.system("pause")
    try:
        with open("farmacia.pickle","rb") as f:
            farmacia=pickle.load(f)
    except FileNotFoundError:
        if not farmacia_creada:
            print("Recuerde crear un producto")
            os.system("pause")
        else:
            print("La farmacia aun no ha sido creada")
            os.system("pause")
    while True:
        try:
            os.system('cls')
            print('FARMACIA UDENAR')
            print('---------------------------------')
            print('   1. Crear farmacia')
            print('   2. Manejo productos')
            print('   3. Manejo ventas ')
            print('')
            print('   4. SALIR')
            print('--------------------------------')
            opcion =int(input('Elija una opción: '))
            match opcion:
                case 1:
                    if not farmacia_creada:
                        farmacia = crear_farmacia()
                        farmacia_creada=True
                        os.system("pause")
                    else:
                        print('Ya ha sido creada la farmacia')
                        os.system("pause")
                case 2:
                    if farmacia_creada==True:
                        manejo_productos(farmacia)
                    else:
                        print('Debe crear la farmacia antes de continuar')
                        os.system("pause")
                     
                case 3:
                    if farmacia_creada==True:
                        manejo_ventas()
                    else:
                        print('Debe crear la farmacia antes de continuar')
                        os.system("pause")
                case 4:
                    print('Volviendo... ')
                    os.system("pause")
                    break
                case other: 
                    print('Ha digitado una opción invalida ')
                    os.system("pause")
        except ValueError:
            print('Digitacion incorrecta, intentelo de nuevo')

def manejo_productos(farmacia):
    while True:
        try:
            os.system('cls')
            print('MANEJO PRODUCTOS')
            print('---------------------------------')
            print('   1. Crear producto')
            print('   2. Mostrar producto ')
            print('   3. Agregar a inventario ')
            print('')
            print('   4. SALIR')
            print('--------------------------------')
            opcion =int(input('Elija una opción: '))
            match opcion:
                case 1:
                    farmacia.registrar_producto()
                case 2:
                    farmacia.mostrar_productos() 
                    os.system("pause")
                case 3:
                    farmacia.pedir_producto()
                case 4:
                    print('Volviendo... ')
                    os.system("pause")
                    break
                case other: 
                    print('Ha digitado una opción invalida ')
                    os.system("pause")
        except ValueError:
            print('Digitacion incorrecta, intentelo de nuevo')


def manejo_ventas():
    while True:
        try:
            os.system('cls')
            print('MANEJO VENTAS')
            print('---------------------------------')
            print('   1. Realizar venta')
            print('   2. Buscar venta (factura) ')
            print('   3. Total de ventas ')
            print('')
            print('   4. SALIR')
            print('--------------------------------')
            opcion =int(input('Elija una opción: '))
            match opcion:
                case 1:
                    manejo_productos()
                case 2:
                    manejo_ventas() 
                case 3:
                    pass
                case 4:
                    print('Volviendo... ')
                    os.system("pause")
                    break
                case other: 
                    print('Ha digitado una opción invalida ')
                    os.system("pause")
        except ValueError:
            print('Digitacion incorrecta, intentelo de nuevo')

main()