print("Hello World") # console.log()
print('magia de serp[iente]')


#tipo de datos
# numeros --> 
1
0.5

#string --> 
'texto'
"texto"

#bol
True
False

None #--> null

#array --> list
[1,2,3] #--> array de toda la vida
(1,2,3) # --> tupla  --> NO ES MUTABLE
{1,2,3} # --> set  --> solo puede tener elementos unicos {1,1,2,3} 

#obj --> diccionarios
{
    'key': 'value'
}

#objeto --> es una referencia a memoria

# entorno se va a encargar de que lo que se instale con PIP se instale SOLAMENTE en el entorno, 
# privativo del proyecto
# gestores de entornos virtuales
# pipenv --> MUY MUY MUY parecido a npm
# venv 


#variables....

var = 'pepe'
#convenio para las constantes, mayusculas
VAR = 'lola'

#nombre --> snake_case

num_one = 5
num_two = 10 
num_three = 5
num_five = None # como el null
#operaciones matematicas
# + - * / 


# operadores logicos
# < > <= >= 
# && and || or
print(num_one < num_two)
print(num_one > num_two)
print(num_one >= num_three)
print(num_one <= num_three)
print(num_one == num_three)
print(num_one is num_three)
print(num_one is not num_three)
print(num_one != num_three)
#print(num_one is num_three)
print(num_one and "hola") ## var && 'hola
print(num_five or 'no existe')

#condiciones

#OJO CON LA INDENTACION --> define el bloque de codigo de python
if num_five:
    print('num five tiene valor', num_five)
#aplicamos la negacion del valor    
if not num_five: # if (!num_five){}
    print('num five NO tiene valor', num_five)

if num_five:
    print('num five tiene valor', num_five)
else:
    print('estoy en el else')
    print(f"valor de one es {num_one} y valor de two es {num_two}") #texto preformateado ( `` en js)
    print(f'valor de one es {num_one} y valor de two es {num_two}') #texto preformateado ( `` en js)

    
if num_five:
    print('num five tiene valor', num_five)
elif num_one and num_two: # else if(){}
    print('estoy en elif con num one y num two')
else:
    print('estoy en el else')


#funciones - definiciones
#declaracion de funcion
#sin return
def myFunc ():
    print('mi primera funcion en python, que emocion')
#ejecucion
myFunc()

def myTopFunc ():
    return 'mi segunda funcion en python, que emocion'

print(myTopFunc())

def paramFunc (param): 
    print(param)
    return param

paramFunc('pepe')

def sumaMalIndentada (a, b):
    total = a+b
    return (total)

def funCondicional (age):
    if age> 15:
        return 'puede manejar'
    return 'no puede manejar'

print(funCondicional(24))


#prompt en python es directamente "input"
# la_edad = input('tu edad?')
# print('en diez años tendras', int(la_edad)+10)

# js --> 'lola' + 10 --> lola10
# py ---> 'lola' + str(10) --> lola10

# en python solo se pueden concatenar TEXTOS, no puede ser texto con numero

#loops
#supuesto 1: quiero iterar 10 veces
for x in range(10):
    #de 0 a 9
    print(x)
for x in range(5,10):
    # de 5 a 9
    print(x)
for x in range(0,10,3):
    #de 0 a 9 de 3 en 3
    print(x)

lista = [1,2,3,4,5,6]
#saber largo se usa len(variable)
print('largo de la lista ',len(lista))#lista.length()

names = ['pepe', 'lola', 'maria', 'matia', 'barbara']

for x in names:
    print(x) #valores

#iterar por las posiciones
# para x dentro del rango del largo de la lista names
for x in range(len(names)): #len(names) === names.length
    if (x < 3):
        print(names[x])

 