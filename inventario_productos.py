#este es un proyecto de prueba para cargar los cambios github
inventario={}

def agregar_producto():
    nombre=input("ingrese el nombre del producto: ").strip().lower()
    
    if nombre in inventario:
        print(f"el producto {nombre} ya se encuentra en el inventario")
        return
    try:
        precio=float(input("ingrese el precio del producto: "))
        cantidad=int(input("ingrese la cantidad del producto: "))
    except ValueError:
        print("ingrese un valor numerico valido")
    
    inventario[nombre]={"precio":precio,"cantidad":cantidad}
    print(f"el producto {nombre} se ha agregado al inventario correctamente")

def buscar_producto():
    nombre=input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
    
    if nombre not in inventario:
        print(f"El producto {nombre} no se encuentra en el inventario")
    else:
        print(f"Producto: {nombre}")
        print(f"Precio: {inventario[nombre]['precio']:.2f}")
        print(f"Cantidad: {inventario[nombre]['cantidad']}")
        
def actualizar_datos():
    nombre=input("Ingrese el nombre del producto que desea actualizar: ").strip().lower()
    
    if nombre not in inventario:
        print(f"El producto {nombre} no se encuentra en el inventario")
        return
    producto=inventario[nombre]
    campos=list(producto.keys())
    
    try:
            #seleccion=input("¿que desea actualizar? (precio/cantidad): ").strip().lower()
            
            #if seleccion=="precio":
                #nuevo_precio=float(input("ingrese el nuevo precio:"))
                #inventario[nombre]["precio"]=nuevo_precio
                #print(f"El precio del producto {nombre} se ha actualizado a {nuevo_precio}")
            #elif seleccion=="cantidad":
                #nueva_cantidad=int(input("ingrese la nueva cantidad: "))
                #inventario[nombre]["cantidad"]=nueva_cantidad
                #print(f"La cantidad de {nombre} se ha actualizado a {nueva_cantidad}")
            #else:
                #print("opcion invalida")
        #except ValueError:
            #print("ingrese un valor numerico valido")
            for i, llave in enumerate(campos, 1):
                print(f"{i}. {llave} (Actual: {producto[llave]})")
            seleccion=int(input(f"Seleccione el numero que desea actualizar: "))
            if seleccion < 1 or seleccion > len(campos):
                print("Error: Seleccion invalida")
                return
            campo_elegido=campos[seleccion-1]
            nuevo_valor=input(f"ingrese el nuevo valor para '{campo_elegido}': ").strip()
            if type(producto[campo_elegido]=='float'):
                nuevo_valor=float(nuevo_valor)
            elif type(producto[campo_elegido]=='int'):
                nuevo_valor=int(nuevo_valor)
            producto[campo_elegido]=nuevo_valor
            print(f"El campo{campo_elegido} ha sido actualizado correctamente")
            
    except ValueError:
            print("ingrese un valor numerico valido")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
                    
def menu():
    while True:
        print("\n---Menu---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar datos")
        print("4. Salir")
        
        opcion=input("Selecciona una opcion: ")
        
        if opcion=="1":
            agregar_producto()
        elif opcion=="2":
            buscar_producto()
        elif opcion=="3":
            actualizar_datos()
        else:
            print("opcion invalida")
            

if __name__ == "__main__":
  menu()