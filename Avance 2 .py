#Menu de inicio (pendiente)

print("Bienvenid@, elige el cálculo que deseas realizar")





#funcion de conversion
def conversiones(conversiones_masa, kg=None, gm=None):
    
    if conversiones_masa == "1":
        kg_gm = kg * 1000
        return(kg_gm)
        
    elif conversiones_masa == "2":
        gm_kg = gm / 1000
        return(gm_kg)
        
    elif conversiones_masa == "3":
        kg_lb = kg * 2.6
        return(kg_lb)
        
    else:
        return "Elija de nuevo"

def conversion_temp(conversiones_temperatura, celsius= None, kelvin= None):
        
    if conversiones_temperatura == 1:
        celsius_kelvin = celsius + 273.5
        return celsius_kelvin

        
    elif conversiones_temperatura == 2:
        kelvin_celsius = kelvin - 273.5
        return kelvin_celsius
        
    else:
        return "Elija de nuevo"
    
#funcion de masa molar            
            
def masa_molar(masa, masa_molecular):
    return masa / masa_molecular

            
#funcion de enlace quimico

def enlace_quimico(electronegatividad_elemento_1, electronegatividad_elemento_2):
    return abs(electronegatividad_elemento_1 - electronegatividad_elemento_2)

            
""" Las siguientes funciones son para almacenar todos los datos necesarios para los calculos
"""

"""
Estas funciones son para el calculo de la masa
"""

#funcion para definir el tipo de conversion de masa 
def inputs_conversiones_masa():
    
    conversiones_masa = input(' Escriba 1 para convertir kg a gm:\n '
                                        'Escriba 2 para convertir gm a kg:\n ' 
                                        'Escriba 3 para convertir kg a lb:\n ' )
    return conversiones_masa

#funcion para pedir los datos de conversion de masa 1

def conversion_masa_1():       
    kg = float(input('Ingrese la cantidad de kg:\n '))
    return kg


#funcion para pedir los datos de conversion masa 2
    
def conversion_masa_2():       
    gm = float(input('Ingrese la cantidad de gms:\n '))
    return gm




                            
"""
Las siguientes funciones son para el calculo de temperatura
"""

#inputs para definir tipo de conversion de temperatura
    
def inputs_conversiones_temperatura():
    
    conversiones_temperatura = int(input('Escriba 1 para convertir grados celsius a kelvin\n'
                                                    'Escriba 2 para convertir grados kelvin a celsius\n '))
    return conversiones_temperatura

#funcion para pedir datos de conversion de temperatura 1

def conversion_temperatura_1():

    celsius = float(input('Ingrese la cantidad de grados celsius\n '))
    return  celsius

#funcion para pedir datos de conversion temperatura 2

def conversion_temperatura_2():
    kelvin = float(input('Ingrese la cantidad de grados kelvin\n '))
    return kelvin

"""
La siguiente funcion es para la masa molar

"""

#funcion para pedir datos de la funcion de masa molar
def datos_masa_molar():
    masa = float(input("Ingrese la masa total del compuesto\n "))
    masa_molecular = float(input("Ingrese la masa molecular total del compuesto\n "))
    return masa, masa_molecular

"""
La siguiente funcion es para la electronegatividad
"""

#funcion para pedir datos de la funcion de electronegatividad
def datos_electro():
    
    electronegatividad_elemento_1 = float(input("Ingrese el número de electronegatividad del primer elemento\n "))
    electronegatividad_elemento_2 = float(input("Ingrese el número de electronegatividad del segundo elemento\n "))
    return electronegatividad_elemento_1,electronegatividad_elemento_2

def imprimir_res(resultado):
    print("Resultado", resultado)
    

#Menu


def menu():
        
    while True:
        
        
        calculo = int(input("Escriba 1 para realizar conversiones de masa  \n"
                            "Escriba 2 para realizar conversiones de temperatura \n"
                    "Escriba 3 para calcular la masa molar de un compuesto: \n"
                    "Escriba 4 para calcular la diferencia de electronegatividad en un enlace:\n"
                            "Escriba 0 para salir: \n"))
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


        else:
            resultado = "opcion no valida"
            
        imprimir_res(resultado)
 
            

menu()

