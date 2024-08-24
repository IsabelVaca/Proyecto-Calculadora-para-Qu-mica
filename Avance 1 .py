#variables permanentes



#Menu de inicio (pendiente)

print("Bienvenid@, elige el cálculo que deseas realizar")




def conversiones():
    tipo_de_conversion = input('Qué tipo de conversión desea realizar?\n'
                               'Escriba 1 para convertir masa\n'
                               'Escriba 2 para convertir temperatura')
    if tipo_de_conversion == '1':
        conversiones_masa = int(input(' Escriba 1 para convertir kg a gm\n'
                                        'Escriba 2 para convertir gm a kg\n'
                                        'Escriba 3 para convertir kg a lb' ))
        if conversiones_masa == 1:
            kg = float(input('Ingrese la cantidad de kg'))
            kg_gm = kg * 1000
            print(kg_gm)
            return(kg_gm)
        
        elif conversiones_masa == 2:
            gm = float(input('Ingrese la cantidad de gms'))
            gm_kg = gm / 1000
            print(gm_kg)
            return(gm_kg)
        
        elif conversiones_masa == 3:
            kg = float(input('Ingrese la cantidad de kg'))
            kg_lb = kg * 2.6
            print(kg_lb)
            return(kg_lb)
        
        else:
            print('Elija de nuevo')
            
             
            
            
        
    elif  tipo_de_conversion == 2:
        conversiones_temperatura = int(input('Escriba 1 para convertir grados celsius a kelvin\n'
                                         'Escriba 2 para convertir grados kelvin a celsius'))
        if conversiones_temperatura == 1:
            celsius = float(input('Ingrese la cantidad de grados celsius'))
            celsius_kelvin = celsius + 273.5
            return celsius_kelvin
            print(celsius_kelvin)
        
        elif conversiones_temperatura == 2:
            kelvin = float(input('Ingrese la cantidad de grados kelvin'))
            kelvin_celsius = kelvin - 273.5
            return kelvin_celsius
            print(kelvin_celsius)
        
        else:
            print('Elija de nuevo')
            
print(conversiones())          
            
                           
            
        
        
                
        
            
        
        
    
    


