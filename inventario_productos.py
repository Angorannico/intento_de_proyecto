#este es un proyecto de prueba para cargar los cambios github
inventario={}

def agregar_producto():
    nombre=input("ingrese el nombre del producto: ").strip().lower()
    
    if nombre in inventario:
        print(f"el producto {nombre} ya se encuentra en el inventario")
    try:
        precio=float(input("ingrese el precio del producto: ")).strip().lower()
        cantidad=int(input("ingrese la cantidad del producto: ")).strip().lower()
    except ValueError:
        print("ingrese un valor numerico valido")
    
    inventario[nombre]={"precio":precio,"cantidad":cantidad}
    print(f"el producto {nombre} se ha agregado al inventario correctamente")
