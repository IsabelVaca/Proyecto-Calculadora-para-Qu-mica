#variables permanentes



#Menu de inicio (pendiente)

print("Bienvenid@, elige el cálculo que deseas realizar")



#funcion de conversion
def conversiones(tipo_de_conversion):
    if tipo_de_conversion == '1':
        
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
            print('Elija de nuevo')

        
    elif  tipo_de_conversion == '2':
        
        if conversiones_temperatura == 1:
            celsius_kelvin = celsius + 273.5
            return celsius_kelvin

        
        elif conversiones_temperatura == 2:
            kelvin_celsius = kelvin - 273.5
            return kelvin_celsius
        
    else:
        print("elija de nuevo")
    
            
            
def masa_molar(masa, masa_molecular):
    calculo_masa_molar = masa / masa_molecular
    return calculo_masa_molar

            
                           
def enlace_quimico(electronegatividad_elemento_1, electronegatividad_elemento_2):
    diferencia_electronegatividad = electronegatividad_elemento_1 - electronegatividad_elemento_2
    diferencia_electronegatividad = abs(diferencia_electronegatividad)
    return diferencia_electronegatividad

    


calculo = int(input("Escriba 1 para realizar conversiones de masa o temperatura: \n"
                    "Escriba 2 para calcular la masa molar de un compuesto: \n"
                    "Escriba 3 para calcular la diferencia de electronegatividad en un enlace:\n "))



#inputs de las variables por funcion 

if calculo == 1:
    tipo_de_conversion = input('Que tipo de conversión desea realizar?\n '
                               'Escriba 1 para convertir masa:\n '
                               'Escriba 2 para convertir temperatura:\n ')
    if tipo_de_conversion == '1':
        conversiones_masa = input(' Escriba 1 para convertir kg a gm:\n '
                                'Escriba 2 para convertir gm a kg:\n ' 
                                'Escriba 3 para convertir kg a lb:\n ' )
        if conversiones_masa == "1":
            kg = float(input('Ingrese la cantidad de kg:\n '))
            
        elif conversiones_masa == "2":
            gm = float(input('Ingrese la cantidad de gms:\n '))
        
        elif conversiones_masa == "3":
            kg = float(input('Ingrese la cantidad de kg:\n'))
                    
        print("Resultado de la conversión:", conversiones(tipo_de_conversion))    

    elif tipo_de_conversion == '2':
        conversiones_temperatura = int(input('Escriba 1 para convertir grados celsius a kelvin\n'
                                            'Escriba 2 para convertir grados kelvin a celsius\n '))
        
        if conversiones_temperatura == 1:
            celsius = float(input('Ingrese la cantidad de grados celsius\n '))
        
        elif conversiones_temperatura == 2:
            kelvin = float(input('Ingrese la cantidad de grados kelvin\n '))
            print(conversiones(tipo_de_conversion))
    
     
        print("Resultado de la conversión:", conversiones(tipo_de_conversion))   

    else:
        print("no valida")
   

elif calculo == 2:
    masa = float(input("Ingrese la masa total del compuesto\n "))
    masa_molecular = float(input("Ingrese la masa molecular total del compuesto\n "))
    print(masa_molar(masa, masa_molecular))
    
elif calculo == 3:
    electronegatividad_elemento_1 = float(input("Ingrese el número de electronegatividad del primer elemento\n "))
    electronegatividad_elemento_2 = float(input("Ingrese el número de electronegatividad del segundo elemento\n "))
    print(enlace_quimico(electronegatividad_elemento_1, electronegatividad_elemento_2))


else:
    print("opcion no valida")
    
    
    
    
    

 
        
        
    
    


