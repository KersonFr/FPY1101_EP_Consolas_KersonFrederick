def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")



def agregar_consola(diccionario_consolas, diccionario_ventas):
    
    sigla=input("Ingrese la sigla: ")
    while not validar_sigla(sigla,diccionario_consolas):
        print("error: no puede estar ingresada,debe tener 2 o 5 caracteres y ser mayuscula")
        sigla=input("Ingrese la sigla: ")

    nombre=input("Ingrese el nombre: ")
    while not validar_texto(nombre,3,40):
        print("error: debe tener 3 o 40 caracteres")
        nombre=input("Ingrese el nombre: ")
    
    fabricante=input("Ingrese el fabricante: ")
    while not validar_texto(fabricante,2,30):
        print("error: debe tener entre 3 o 4 caracteres")
        fabricante=input("Ingrese el fabricante: ")
    
    año=input("Ingrese el año de lanzamiento: ")
    while not validar_año(año):
        print("error: debe ser un numero entero entre 1972 o 2025")
        año=input("Ingrese el año de lanzamiento: ")
    
    precio=input("Ingrese el precio: ")
    while not validar_precio(precio):
        print("error: precio invalido, debe ser un numero decimal mayor a 0")
        precio=input("Ingrese el precio: ")
    
    stock=input("Ingrese el stock: ")
    while not validar_stock(stock):
        print("error: debe ser un numero entero mayor o igual a 0")
        stock=input("Ingrese el stock: ")
    

    diccionario_consolas[sigla]=[nombre,fabricante,int(año)]
    diccionario_ventas[sigla]=[float(precio),int(stock)]
    print(f"se agrego la sigla: {sigla}")


def validar_año(año_texto):
    if not año_texto.isdigit():
        return False
    año_numero=int(año_texto)
    if año_numero<1972 or año_numero>2025:
        return False
    return True



def validar_precio(precio_texto):
    #esta validacion la busqe en internet, no la conocia la verdad.
    if not precio_texto.replace('.','',1).isdigit():
        return False
    numero=float(precio_texto)
    if numero<=0:
        return False
    return True


    
        
def validar_stock(stock_texto):
    if not stock_texto.isdigit():
        return False
    numero=int(stock_texto)
    if numero <0:
        return False
    return True

def validar_texto(texto,minimo,maximo):
    if len(texto)<minimo or len(texto)>maximo:
        return False
    return True
    
def validar_sigla(sigla,diccionario_consolas):
    if len(sigla)<2 or len(sigla)>5:
        return False
    if not sigla.isupper():
        return False
    if sigla in diccionario_consolas:
        return False
    return True

def solicitar_opcion():
    opcion_ingresada = input("Seleccione una opción (1-5): ")
    return opcion_ingresada

def buscar_consola(diccionario_consolas,diccionario_ventas):
    print("--cual busca--")
    sigla=input("Ingrese la sigla: ")
    if sigla in diccionario_consolas:
        print(diccionario_consolas[sigla])
        print(diccionario_consolas[sigla][0])
        print(diccionario_consolas[sigla][1])
        print(diccionario_consolas[sigla][2])
        print(diccionario_ventas[sigla][0])
        print(diccionario_ventas[sigla][1])
    else:
        print("no se encontro")

def eliminar(diccionario_consolas,diccionario_ventas):
    print("cual va a eliminar")
    sigla=input("Ingrese la sigla: ")
    if sigla in diccionario_consolas:
        del(diccionario_consolas[sigla])
        del(diccionario_ventas[sigla])
        print("se borro")
    else:
        print("no se encontro")

def mostrar_todo(diccionario_consolas,diccionario_ventas):
    if len(diccionario_consolas)==0:
        print("no hay nada")
    else:
        print("==============================")
        print("LISTADO COMPLETO DE CONSOLAS")
        print("==============================")
        for sigla in diccionario_consolas:
            consola=diccionario_consolas[sigla]
            ventas=diccionario_ventas[sigla]
            print(f"sigla:{sigla}|{consola[0]}|{consola[1]}|{consola[2]}|{ventas[0]}|{ventas[1]}")
        print("==============================")
        print(f"total de consola: {len(diccionario_consolas)}")




def menu():

    diccionario_consolas = {}
    diccionario_ventas = {}


    while True:
        mostrar_menu()
        opcion = solicitar_opcion()
        
        if opcion == "1":
            agregar_consola(diccionario_consolas,diccionario_ventas)
        elif opcion == "2":
            buscar_consola(diccionario_consolas,diccionario_ventas)
        elif opcion == "3":
            eliminar(diccionario_consolas,diccionario_ventas)
        elif opcion == "4":
            mostrar_todo(diccionario_consolas,diccionario_ventas)
        elif opcion == "5":
            print("Saliendo... ¡Hasta pronto!")
            break
        else:
            print("Opción inválida, intente nuevamente.")


menu()# Modulo de validaciones
# Modulo agregar consola
