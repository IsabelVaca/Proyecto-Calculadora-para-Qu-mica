# Proyecto-Calculadora-para-Quimica

Para mi proyecto de la materia decidí hacer una calculadora para calcular conceptos de Química, como por ejemplo: 
-Calcular la masa molar de una sustancia
-Calcular electronegatividad de un enlace 
-Convertir temperaturas y peso
-Calcular el peso molecular de un compuesto
-Encontrar numero atomico de un elemento
-Consultar datos de los diferentes tipos de celdas cúbicas de los sólidos


En esta calculadora el usuario tendrá la opción de elegir entre las diferentes funciones de la calculadora dentro de un menú principal donde se desplegarán las diferentes opciones. 

Este proyecto me parece interesante ya que durante este semestre estoy llevando clases de química en donde es necesario realizar varios cálculos y en algunos casos he tenido que recurrir a páginas que hacen conversiones de peso o energía, por ende este proyecto no solo puede ser bastante útil para personas que estan estudiando algún curso de química pero en mi caso me ayudará a repasar los conceptos y entenderlos de una mejor manera.
Este proyecto me permite desarrollar mis habilidades y demostrar mis conocimientos por medio de la aplicación de operadores, ciclos, condiciones, funciones, etc. 

# Algoritmo

EI (menú donde se presentan todos los cálculos que la calculadora puede realizar de manera enumerada y el usuario tendrá qué elegir el que desee realizar)

Listas de elementos de la tabla periodica y de numeros atomicos

Matriz con datos de celdas cubicas

Se definirá una función para cada cálculo en órden

Se definen funciones para inputs

Cada funcion tendrá su número o clave asignada con la que será identificada después de ser seleccionada por el usuario

Cada función pedirá al usuario la información necesaria para realizar los cálculos 

funcion de menu que funciona por medio de un ciclo que desplega los calculos con if statements y va mostrando resultados

EF(el resultado de los cálculos solicitados hasta que se decida cerrar la calculadora)

# Temas extra
En mi proyecto investigue varias cosas extra que me ayudaron en el desarrollo de mi proyecto
1 funcion abs() usada para el resultado de la electronegatividad. Fuente: W3schools

2 Parametro Default En las funciones de conversiones tuve problemas con los parametros ya que no siempre usaba todos

asi que decidi definir unos por default en caso de que no se pasara dicho parametro y no saliera un error. Fuente: W3schoos Python Functions
3 try: except: esto lo use para en caso de que se ingresara un tipo de dato no válido en los inputs. https://docs.python.org/es/3/tutorial/errors.html

4 isinstance() esta funcion la utilice para que en caso de que un input tuviera un dato invalido y que en try: except ValueError: si salia un error y se desplegara el mensaje
"entrada no valida" no se hicieran las proximas operaciones, y antes de hacerlas verificar que el dato de la variable es correcto. https://www.startdataengineering.com/post/how-to-validate-datatypes-in-python/

# Modo de uso
Descargar archivo y correr en terminal

Ingresar Python Avance 2.py

o en Thonny y dar play

Elegir las operaciones deseadas y dar los datos que se piden 
