#listas de elementos y lista de sus numeros atomicos
elementos = [ "H", "He", "Li", "Be","B", "C", "N", "O", "F", "Ne", "Na"
              "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti",
              "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As",
              "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru",
              "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
              "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
              "Ti", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Rf", "Db"
              "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv",
              "Ts", "Og"]
lista_numeros_atomicos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,28,19,20,21,
                          22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
                          40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,
                          58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,
                          76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,92,93,94,
                          95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,
                          110,111,112,113,114,115,116,117,118]

#Lista anidada de los tipos de celdas cubicas
"""
El indice 0 indica el numero de atomos por celda, el indice 1 indica el numero de
coordinacion y el indice 2 indica el porcentaje de eficiencia de empaquetado
"""
celda_cubica_simple = [1,6,52]
celda_cubica_centrada_en_el_cuerpo = [2,8,68]
celda_cubica_centrada_en_las_caras = [4,12,74]

celdas_cubicas = [ celda_cubica_simple, celda_cubica_centrada_en_el_cuerpo, celda_cubica_centrada_en_las_caras]


#funcion de conversion
"""
Esta funcion toma como parametros el indice de la conversion de la masa(1 para convertir kg a gm, el 2
es para convertir gm a kg, el 3 para convertir kg a lb.
Toma los kilo gramos para hacer las conversiones 1 y 3. Toma los gramos para la conversion 2.
"""

def conversiones(conversiones_masa, kg=None, gm=None):
    
    if conversiones_masa == "1":
        return kg * 1000
        
    elif conversiones_masa == "2":
        return gm / 1000
        
    elif conversiones_masa == "3":
        return kg * 2.6
        
    else:
        return "Elija de nuevo"

#Funcion de conversion de temperatura    
"""
Esta funcion toma como parametros el indice de conversion de temperatura, grados celsius y kelvin, estos datos se
piden al usuario en la funcion de menu en el calculo 2
"""
       
def conversion_temp(conversiones_temperatura, celsius= None, kelvin= None):
        
    if conversiones_temperatura == 1:
        return celsius + 273.5

        
    elif conversiones_temperatura == 2:
        return kelvin - 273.5
        
    else:
        return "Elija de nuevo"
    
    
    
#funcion de masa molar
"""
Esta funcion toma como parametros la masa y la masa molecular, estos datos son pedidos al usuario en la funcion menu
si el usuario elige el calculo 3
"""
                
def masa_molar(masa, masa_molecular):
    return masa / masa_molecular

            
#funcion de enlace quimico
"""
Esta funcion tiene como parametros las dos electronegatividades de los dos elementos, luego las resta y saca el valor absoluto
para poder calcular el la electronegatividad del enlace quimico
"""

def enlace_quimico(electronegatividad_elemento_1, electronegatividad_elemento_2):
    return abs(electronegatividad_elemento_1 - electronegatividad_elemento_2)


#Funcion para encontrar el numero atomico de un elemento
"""
Esta funcion toma como parametro el nombre de un elemento y devuelve el numero atomico de dicho elemento
"""

def encuentra_numero_atm(elemento):
    indice = elementos.index(elemento)     
    return lista_numeros_atomicos[indice]

def datos_celdas_cubicas(celda_cubica, dato_celda_cub):

    if celda_cubica == 1: 
        if dato_celda_cub == 1:
            return celdas_cubicas[0][0]
        elif dato_celda_cub == 2:
            return celdas_cubicas[0][1]
        elif dato_celda_cub == 3:
            porcentaje = str(celdas_cubicas[1][2])
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
            porcentaje = str(celdas_cubicas[1][2])
            return porcentaje + str("%")
    else:
        return "intentelo de nuevo"

        
                
                        
    
 
""" Las siguientes funciones son para almacenar todos los datos necesarios para los calculos,
    Decidí crear una funcion por operación para que dependiendo del calculo el texto que apareciera
    pidiera la informacion de manera mas especifica, esto es para que sea mas facil de usar y para ingresar
    los datos correctos. 
"""

"""
Estas funciones son para el calculo de la masa
"""

#funcion para definir el tipo de conversion de masa
def inputs_conversiones_masa():
    
    conversiones_masa = input(' Escriba 1 para convertir kg a gm: \n '
                                        'Escriba 2 para convertir gm a kg: \n ' 
                                        'Escriba 3 para convertir kg a lb: \n ' )
    return conversiones_masa

#funcion para pedir los datos de conversion de masa 1
def conversion_masa_1():       
    kg = float(input('Ingrese la cantidad de kg: \n '))
    return kg

#funcion para pedir los datos de conversion masa 2    
def conversion_masa_2():       
    gm = float(input('Ingrese la cantidad de gms: \n '))
    return gm
                            
"""
Las siguientes funciones son para el calculo de temperatura
"""

#inputs para definir tipo de conversion de temperatura   
def inputs_conversiones_temperatura():
    
    conversiones_temperatura = int(input('Escriba 1 para convertir grados celsius a kelvin \n'
                                                    'Escriba 2 para convertir grados kelvin a celsius \n '))
    return conversiones_temperatura

#funcion para pedir datos de conversion de temperatura 1
def conversion_temperatura_1():

    celsius = float(input('Ingrese la cantidad de grados celsius \n '))
    return  celsius

#funcion para pedir datos de conversion temperatura 2
def conversion_temperatura_2():
    kelvin = float(input('Ingrese la cantidad de grados kelvin \n '))
    return kelvin

#funcion para pedir datos de la funcion de masa molar
def datos_masa_molar():
    masa = float(input("Ingrese la masa total del compuesto \n "))
    masa_molecular = float(input("Ingrese la masa molecular total del compuesto \n "))
    return masa, masa_molecular

#funcion para pedir datos de la funcion de electronegatividad
def datos_electro():
    
    electronegatividad_elemento_1 = float(input("Ingrese el número de electronegatividad del primer elemento \n "))
    electronegatividad_elemento_2 = float(input("Ingrese el número de electronegatividad del segundo elemento \n "))
    return electronegatividad_elemento_1,electronegatividad_elemento_2

#Funcion para pedir el elemento del calculo 5 
def elemento_en_tabla_periodica():
    elemento = str(input("Ingrese la abreviatura del nombre del elemento, la primera letra debe ser mayuscula \n"))
    return elemento

#Funcion para pedir el tipo de celda cubica y el dato a buscar
def pide_datos_celda_cub():
    celda_cubica = int(input("Ingrese 1 para consultar datos de celda cubica simple \n"
                         "Ingrese 2 para consultar datos de celda cubica centrada en el cuerpo \n"
                         "Ingrese 3 para consultar datos de celda cubuca centrada en las caras \n"))
    dato_celda_cub = int(input("Ingrese 1 para consultar el numero de atomos por celda \n"
                               "Ingrese 2 para consultar el numero de coordinacion \n"
                               "Ingrese 3 para consultar el porcentaje de eficiencia de empaquetado \n"))
    return celda_cubica,dato_celda_cub

#Funcion para imprimir los resultados
def imprimir_res(resultado):
    print("El resultado es ", resultado,
          "\n ")
    

#Menu


def menu():
        
    while True:
        
        
        calculo = int(input("Bienvenid@, elige el cálculo que deseas realizar \n"
                            "Escriba 1 para realizar conversiones de masa  \n"
                            "Escriba 2 para realizar conversiones de temperatura \n"
                    "Escriba 3 para calcular la masa molar de un compuesto \n"
                    "Escriba 4 para calcular la diferencia de electronegatividad en un enlace\n"
                            "Escriba 5 para encontrar el numero atomico de un elemento \n"
                            "Escribe 6 para consultar datos sobre los tipos de celdas cubicas de los solidos \n"
                            "Escriba 0 para salir \n"))
        if calculo == 0:
            print("Saliendo de la calculadora")
            break
        
        
        elif calculo == 1:
            
            conversiones_masa = inputs_conversiones_masa()
                
            if conversiones_masa == "1":
                kg = conversion_masa_1()
                resultado = conversiones(conversiones_masa, kg=kg)
                    
            elif conversiones_masa == "2":
                gm = conversion_masa_2()
                resultado = conversiones(conversiones_masa, gm=gm)
                
            elif conversiones_masa == "3":
                kg = conversion_masa_1()                 
                resultado = conversiones(conversiones_masa, kg=kg)
            
            else:
                resultado = "intenta otra vez"
                
                
        elif calculo == 2:
               
            conversiones_temperatura = inputs_conversiones_temperatura()
                
            if conversiones_temperatura == 1:
                celsius = conversion_temperatura_1()
                resultado = conversion_temp(conversiones_temperatura, celsius)
                
            elif conversiones_temperatura == 2:
                kelvin = conversion_temperatura_2()
                resultado = conversion_temp(conversiones_temperatura, kelvin)
            else:
                resultado = "intenta otra vez"
          

        elif calculo == 3:
            masa, masa_molecular = datos_masa_molar()
            resultado = masa_molar(masa, masa_molecular)
            
        elif calculo == 4:
            electronegatividad_elemento_1, electronegatividad_elemento_2 = datos_electro()
            resultado = enlace_quimico(electronegatividad_elemento_1, electronegatividad_elemento_2)
            
        elif  calculo == 5:
            elemento = elemento_en_tabla_periodica()
            if elemento in elementos:
                
                resultado = encuentra_numero_atm(elemento)
            else:
                resultado = "Ingrese el nombre de nuevo"
                
        elif calculo == 6:
            celda_cubica,dato_celda_cub = pide_datos_celda_cub()
            resultado = datos_celdas_cubicas(celda_cubica, dato_celda_cub)
       
        else:
            resultado = "opcion no valida"
            
        imprimir_res(resultado)

#inicia calculadora
            
menu()
print(celdas_cubicas[0][2])


