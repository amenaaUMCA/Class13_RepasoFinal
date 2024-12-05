#Proyecto clase 13 Reapso Final
#Autor: Andrés Mena A.
import csv
import pandas as pd
import os

def menu():
    ventas = []
    while True:
        print('\n ---- Menú Principal ---')
        print('1. Ingresar datos de ventas.')
        print('2. Guardar datos en un archivo CSV.')
        print('3. Analizar los datos guardados.')
        print('4. Salir del sistema.')
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            print('\n ---- Ingreso de Ventas ---')
            ingresar_datos(ventas)
        elif opcion == '2':
            print('\n ---- Guardar datos de Ventas ---')
            guardar_csv(ventas)            
        elif opcion == '3':
            print('\n ---- Analizar las Ventas ---')
            analizar_ventas(ventas)
        elif opcion == '4':
            print('\n Saliendo del sistema. Hasta pronto!')
            break
        else:
            print('Opción no válida. Vuelva a intentarlo.')

def analizar_ventas(ventas):
    df = pd.read_csv('ventas.csv', encoding='latin-1') 
    print('\n --- Resumen de Ventas ---')
    
    #¿Cuál fue el total de ingresos generados?
    df['Subtotal'] = df['Cantidad'] * df['Precio']
    Total = df['Subtotal'].sum()
    print(f'Total de ingresos ₡{Total:.2f}')

    #¿Cuál fue el producto más vendido?
    producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum().idxmax()
    #cantidad_vendida =  df.groupby('Producto')['Cantidad'].sum()
    print(f'El producto mas vendido es {producto_mas_vendido} con estas unidades ')

    #¿Quién fue el cliente con más compras?
    
    #¿Cuáles fueron las ventas por fecha? -groupby
"""
o	¿Cuál fue el total de ingresos generados?
o	¿Cuál fue el producto más vendido? - 
o	¿Quién fue el cliente con más compras?
o	¿Cuáles fueron las ventas por fecha? -groupby

"""
         
def guardar_csv(ventas):
    if not ventas:
        print('No hay datos para guardar')
        return
    with open('ventas.csv', mode='w',newline='') as file:
        guardado = csv.DictWriter(file,fieldnames=['Producto','Cantidad','Precio','Fecha','Cliente'])
        guardado.writeheader()
        guardado.writerows(ventas)
    print('Datos guardados en el archivo.')
        

def ingresar_datos(ventas):
   while True:
        #Entrada de datos
        producto = input('Ingrese el nombre del producto: ')
        cantidad = int(input('Ingrese la cantidad vendida: '))
        precio = float(input('Ingrese precio por unidad: '))
        fecha = input('Ingrese la fecha de la venta (YYYY-MM-DD): ') #Fecha de la venta en formato YYYY-MM-DD.
        cliente = input('Ingrese el nombre del cliente: ') #Nombre del cliente que realizó la compra.

        #Validaciones con if
        if cantidad <= 0: 
            print('La cantida sebe ser mayor a 0. Inténtelo nuevamente.')
            continue
        if precio <= 0:
            print('Precio no validó. Intételo nuevamente.')
            continue
        venta = {
            'Producto':producto,
            'Cantidad':cantidad,
            'Precio':precio,
            'Fecha':fecha,
            'Cliente':cliente
        }
        ventas.append(venta)
        #Preguntar
        continuar = input('Desea ingresar otra venta? (s/n): ').lower()
        if continuar == 'n':
            break
    
#Validar la ejecución del archivo principal
if __name__ == '__main__':
    print('Bienvenido al sistema de Gestión de Ventas')
    menu()