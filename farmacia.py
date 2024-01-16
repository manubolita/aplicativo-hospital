import pickle
import os
class FARMACO:
    def __init__(self,nombre,id_producto,valor,cantidad):
        self.nombre=nombre
        self.id_producto=id_producto
        self.valor=valor
        self.cantidad=cantidad
    def __str__(self):
        return (f"Nombre producto {self.nombre}, Id producto {self.id_producto}, valor producto {self.valor}, cantidad inventario {self.cantidad}")

class FARMACIA:
    numeroFactura=0
    dinerocaja=0
    id_producto=0
    def __init__(self,productos,factura):
        self.productos=productos
        self.factura=factura
        self.id_producto=1

    def guardar_productos(self):
        with open('productos.pickle', 'wb') as f:
            pickle.dump(self.productos, f)

    def registrar_producto(self):
        while True:
            nombre= input("digite el nombre del producto ---> ")
            if self.buscar_producto(nombre)!=False:
                print("El producto ya existe, imposible agregar producto... ")
            else:
                id_producto = self.id_producto
                self.id_producto+=1
                valor= float(input("Ingrese valor del producto ---> "))
                cantidad=int(input("Cuantas unidades tiene? ---> "))
                producto=FARMACO(nombre,id_producto,valor,cantidad)
                print(f"Producto ---> {producto}")
                self.adicionar_producto(producto)
                self.guardar_productos()
                print("producto ingresado correctamente")
            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                break
    def buscar_producto(self,nombre):
        for p in self.productos:
            if p.nombre == nombre:
                return p
        else:
            return False
    
    def adicionar_producto(self,producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if len(self.productos)>0:
            print("\nLista de Productos\n---------------------")
            for i in range (len(self.productos)):
                print(f"{i+1} - {self.productos[i]}")
        else:
            print("No hay productos disponibles.")
    
    def pedir_producto(self):
        nombre= input("Ingrese el nombre del producto que desea pedir: ")
        if self.buscar_producto(nombre)== False:
            print(f'No se ha encontrado un producto con el nombre: {nombre}')
        else:
            producto = self.buscar_producto(nombre)
            cantidad_pedir= int(input("Ingrese la cantidad que desea pedir: "))
            if cantidad_pedir>0:
                producto.cantidad+= cantidad_pedir
                print (f"Se han agrgado {cantidad_pedir} unidades del producto {nombre} al inventario.")
            else:
                print("La cantidad debe ser mayor a cero. ")
        os.system('pause')
        