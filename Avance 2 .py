 """
Proyecto calculadora de Quimica
Hecho por Isabel Vaca Sanchez A01352522
Este programa realiza calculos de quimica dependiendo de lo que
elija el usuario, el programa pide los datos requeridos y devuelve
el resultado. El programa termina hasta que el usuario elija salir
"""
#listas de elementos lista de sus numeros atomicos
elementos = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
             "Na","Mg", "Al","Si", "P", "S", "Cl", "Ar", "K", "Ca",
             "Sc","Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
             "Ga","Ge","As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
             "Nb","Mo","Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
             "Sb","Te","I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
             "Pm","Sm","Eu", "Gd", "Tb", "Dy", "Ho", "Er","Tm", "Yb",
             "Lu","Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
             "Tl","Pb","Bi", "Po", "At","Rn", "Fr", "Ra", "Ac", 
             "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
             "Es","Fm", "Md", "No","Lr", "Rf", "Db", "Sg", 
             "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
             "Lv","Ts", "Og"]

#Lista de sus numeros atomicos
lista_numeros_atomicos = list(range(1, 119))

#Lista anidada de los tipos de celdas cubicas
"""
El indice 0 indica el numero de atomos por celda, el indice 1
indica el numero de coordinacion y el indice 2 indica el
porcentaje de eficiencia  de empaquetado. 
"""
celda_cubica_simple = [1,6,52]
celda_cubica_centrada_en_el_cuerpo = [2,8,68]
celda_cubica_centrada_en_las_caras = [4,12,74]

celdas_cubicas = [
    celda_cubica_simple, celda_cubica_centrada_en_el_cuerpo,
                   celda_cubica_centrada_en_las_caras]


#funcion de conversion
def conversiones(conversiones_masa, kg=0, gm=0):
    """
    Esta funcion toma como parametros el indice de la
    conversion de la masa(1 para convertir kg a gm, el 2
    es para convertir gm a kg, el 3 para convertir kg a lb.
    Toma los kgms para hacer las conversiones 1 y 3.
    Toma los gm para la conversion 2.
    Devuelve dependiendo la opcion
    
    """
    
    if conversiones_masa == "1":
        return kg * 1000
        
    elif conversiones_masa == "2":
        return gm / 1000
        
    elif conversiones_masa == "3":
        return kg * 2.2
        
    else:
        return "Elija de nuevo"

#Funcion de conversion de temperatura        
def conversion_temp(conversiones_temperatura, celsius=0, kelvin=0):
    """
    Esta funcion toma como parametros el indice de conversion
    de temperatura, grados celsius y kelvin, estos datos se
    piden al usuario en la funcion de menu en el calculo 2
    Los parametros tienen un valor default de 0 en caso de que
    no se requieran todos
    devuelve la conversion dependiendo la opcion
    """     
    if conversiones_temperatura == 1:
        return celsius + 273.15

        
    elif conversiones_temperatura == 2:
        return kelvin - 273.15
        
    else:
        return "Elija de nuevo"
    
    
    
#funcion de masa molar         
def masa_molar(masa, masa_molecular):
    """
    Esta funcion toma como parametros la masa y la masa molecular
    , estos datos son pedidos al usuario en la funcion menu
    si el usuario elige el calculo 3
    devielve masa molar
    """
  
    return masa / masa_molecular

            
#funcion de enlace quimico
def enlace_quimico(electroneg_elemento_1, electroneg_elemento_2):
    """
    Esta funcion tiene como parametros las dos electronegatividades
    de los dos elementos, luego las resta y saca el valor absoluto
    para poder calcular el la electronegatividad del enlace quimico
    devuelve la electronegatividad del enlace quimico
    """

    return abs(electroneg_elemento_1 - electroneg_elemento_2)


#Funcion para encontrar el numero atomico de un elemento

def encuentra_numero_atm(elemento):
    
    """Esta funcion recibe la abreviacion de un elemento, un ciclo
    for recorre toda la lista buscando el elemento, con el indice
    se compara con la lista de numeros atomicos y devuelve el
    numero atomico del elemento
    devuelve el num atomico del elemento
    """
    i = 0
    if elemento in elementos:
        while i < len(elementos):
            if elementos[i] == elemento:
                return lista_numeros_atomicos[i]
            i+=1
    else:
        return "Intente de nuevo"
            

def datos_celdas_cubicas(celda_cubica, dato_celda_cub):
    """
    Esta funcion toma como parametros los inputs del tipo de celda que se
    desea consultar y la categoria que se desea consultar. opcion 1 celda
    cubica simple 1 celda cubica centrada en el cuerpo, 3 celda cubica
    centrada en las caras. la columna 0 representa el num de atomos, la
    2da el num de coordinacion, la 3era el porcentaje de eficiencia
    de empaquetado. Devuelve el dato requerido
    """
    if celda_cubica == 1: 
        if dato_celda_cub == 1:
            return celdas_cubicas[0][0]
        elif dato_celda_cub == 2:
            return celdas_cubicas[0][1]
        elif dato_celda_cub == 3:
            porcentaje = str(celdas_cubicas[0][2])
            return porcentaje + str("%")
            
    elif celda_cubica == 2:
        if dato_celda_cub == 1:
            return celdas_cubicas[1][0]
        elif dato_celda_cub == 2:
            return celdas_cubicas[1][1]
        elif dato_celda_cub == 3:
            porcentaje = str(celdas_cubicas[1][2])
            return porcentaje + str("%")
    
    elif celda_cubica == 3:
        if dato_celda_cub == 1:
            return celdas_cubicas[2][0]
        elif dato_celda_cub == 2:
            return celdas_cubicas[2][1]
        elif dato_celda_cub == 3:
            porcentaje = str(celdas_cubicas[2][2])
            return porcentaje + str("%")
    else:
        return "intentelo de nuevo"

""" Las siguientes funciones son para almacenar todos los datos
necesarios para los calculos, Decidí crear una funcion por operacion
para que dependiendo del  calculo el texto que apareciera pidiera la
informacion demanera mas  especifica, esto es para que sea mas facil
de usar y para ingresar    los datos correctos. 
"""

#Estas funciones son para el calculo de la masa
def inputs_conversiones_masa():
    #funcion para definir el tipo de conversion de masa
   
    conversiones_masa = input(
        ' Escriba 1 para convertir kg a gm: \n '
        'Escriba 2 para convertir gm a kg: \n '
        'Escriba 3 para convertir kg a lb: \n')
    return conversiones_masa

    
def conversion_masa_1():
    """
    funcion para pedir los datos de conversion de masa 1
    """
    try:
        kg = float(input('Ingrese la cantidad de kg: \n '))
        return kg
    except ValueError:
        return "Entrada no valida"
    
def conversion_masa_2():       
    """funcion para pedir los datos de conversion masa 2
    """
    try:
        gm = float(input('Ingrese la cantidad de gms: \n '))
        return gm
    except ValueError:
        return "Entrada no valida"

#Las siguientes funciones son para el calculo de temperatura

def inputs_conversiones_temperatura():
    """
    inputs para definir tipo de conversion de temperatura   
    """
    try:
        conversiones_temperatura = int(input(
            'Escriba 1 para convertir grados celsius a kelvin \n'
         'Escriba 2 para convertir grados kelvin a celsius \n '))
        return conversiones_temperatura
    except ValueError:
        return "Entrada no Valida"
        
def conversion_temperatura_1():
    """
    funcion para pedir datos de conversion de temperatura 1
    """
    try:
            
        celsius = float(input(
            'Ingrese la cantidad de grados celsius \n '))
        return  celsius
    except ValueError:
        return "entrada no valida"
    
def conversion_temperatura_2():
    """
    funcion para pedir datos de conversion temperatura 2
    """
    try:
        kelvin = float(input(
            'Ingrese la cantidad de grados kelvin \n '))
        return kelvin
    except ValueError:
        return "Entrada no valida"

def datos_masa_molar():
    """
    funcion para pedir datos de la funcion de masa molar
    """

    masa = float(input(
            "Ingrese la masa total del compuesto \n "))

    masa_molecular = float(input(
            "Ingrese la masa molecular total del compuesto \n"))
    return masa, masa_molecular

def datos_electro():
    """
    funcion para pedir datos de la funcion de electronegatividad
    """
    electroneg_elemento_1 = float(
        input(
        "Ingrese el número de electronegatividad del primer elemento \n "
        ))
    electroneg_elemento_2 = float(
        input(
        "Ingrese el número de electronegatividad del segundo elemento \n "
        ))
    return electroneg_elemento_1,electroneg_elemento_2

def elemento_en_tabla_periodica():
    """
    Funcion para pedir el elemento del calculo 5
    """
    elemento = str(input(
        "Ingrese la abreviatura del nombre del elemento, \n"
          "la primera letra debe ser mayuscula \n"))
    return elemento

def pide_datos_celda_cub():
    """
    Funcion para pedir el tipo de celda cubica y el dato a buscar
    """
    celda_cubica = int(input(
        "Ingrese 1 para consultar datos de celda cubica simple \n"
        "Ingrese 2 para consultar datos de celda cubica centrada en el cuerpo\n"
        "Ingrese 3 para consultar datos de celda cubuca centrada en las caras\n"))
    dato_celda_cub = int(input(
        "Ingrese 1 para consultar el numero de atomos por celda \n"
        "Ingrese 2 para consultar el numero de coordinacion \n"
     "Ingrese 3 para consultar el porcentaje de eficiencia de empaquetado\n"))
    return celda_cubica,dato_celda_cub

def imprimir_res(resultado):
    """Funcion para imprimir los resultados
    recibe el resultado del calculo y lo imprime
    """
    print("El resultado es ", resultado,
          "\n ")
    

#Menu
def menu():    
    """
    Este menu funciona por medio de un ciclo que desplega todas las opciones
    El usuario elige y dependiendo del calculo se valida la opcion con un if 
    statement, el ciclo sigue hasta que el usuario elija salir de la
    calculadora
    """
    while True:
        
        calculo = int(input(
             "Bienvenid@, elige el cálculo que deseas realizar\n"
                   "Escriba 1 para realizar conversiones de masa\n"
                      "Escriba 2 para conversiones de temperatura\n"
            "Escriba 3 para calcular la masa molar de un compuesto \n"
    "Escriba 4 para calcular la diferencia de electronegatividad en un enlace\n"
              "Escriba 5 para encontrar el numero atomico de un elemento\n"
               "Escribe 6 para consultar datos de los tipos de \n"
               "las celdas cubicas de los solidos \n"
                            "Escriba 0 para salir \n"))
        if calculo == 0:
            print("Saliendo de la calculadora")
            break
        
        
        elif calculo == 1:
            conversiones_masa = inputs_conversiones_masa()
            if conversiones_masa == "1":
                kg = conversion_masa_1()
                if isinstance(kg, float) == True:
                    resultado = conversiones(conversiones_masa, kg, 0)
                else:
                    resultado = kg
                    
            elif conversiones_masa == "2":
                gm = conversion_masa_2()
                if isinstance(gm, float):
                    resultado = conversiones(conversiones_masa, 0, gm)
                else:
                    resultado = gm
            elif conversiones_masa == "3":
                kg = conversion_masa_1()                 
                resultado = conversiones(conversiones_masa, kg, 0)
            
            else:
                resultado = "intenta otra vez"
                
                
        elif calculo == 2:
            conversiones_temperatura = inputs_conversiones_temperatura()
            if isinstance(conversiones_temperatura, int):
                if conversiones_temperatura == 1:
                    celsius = conversion_temperatura_1()
                    if isinstance(celsius, float):
                        resultado = conversion_temp(
                            conversiones_temperatura, celsius)
                    else:
                        resultado = celsius
                elif conversiones_temperatura == 2:
                    kelvin = conversion_temperatura_2()
                    if isinstance(kelvin, float):
                        resultado = conversion_temp(
                            conversiones_temperatura, 0, kelvin)
                    else:
                        resultado = kelvin
                else:
                    resultado = "intenta otra vez"
            else:
                resultado = conversiones_temperatura

        elif calculo == 3:
            masa, masa_molecular = datos_masa_molar()
            if isinstance(masa, float):               
                resultado = masa_molar(masa, masa_molecular)
            else:
                resultado = masa
        elif calculo == 4:
            electroneg_elemento_1, electroneg_elemento_2 = datos_electro()
            resultado = enlace_quimico(
                electroneg_elemento_1, 
                                       electroneg_elemento_2)
            
        elif  calculo == 5:
            elemento = elemento_en_tabla_periodica()
            if elemento in elementos:
                
                resultado = encuentra_numero_atm(elemento)
            else:
                resultado = "Ingrese el nombre de nuevo"
                
        elif calculo == 6:
            celda_cubica,dato_celda_cub = pide_datos_celda_cub()
            resultado = datos_celdas_cubicas(
                celda_cubica, dato_celda_cub)
       
        else:
            resultado = "opcion no valida"
            
            
        imprimir_res(resultado)

#inicia calculadora
            
menu()



