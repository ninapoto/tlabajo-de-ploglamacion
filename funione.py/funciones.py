#funcion: se de intrucciones que ejecuta una tarea especifica
#arg: argumentos con los que va a trabajar la funcion
def saludar(nombre):
    print(f"ola mi nombre es {nombre}")
nombre= input("ingrse su nombre: ")
    
saludar(nombre)

#funcion que ume dos numeros 
def suma(a,b):
    resultado = a + b 
    print(f"el resultado de sumar {a} + {b} = {resultado}")
#DEFINIR VARIABLES
numero_1 = int(input("ingrese su primer numero: "))
numero_2 = int(input("ingrese su segundo numero: "))
#EJECUTAR FUNCION
suma(numero_1,numero_2)

#funcion que multiplique dos numeros 
numero_1 = int(input("ingrese su primer nunmero: "))
numero_2 = int(input("ingrese su segundo numero: "))
operacion = input("ingrese su operacion: ")

def calculadora (a,b,op):
    resultado = 0 
    if op == "+":
        resultado = a + b
    elif op == "*":
        resultado = a * b 
    elif op == "-":
        resultado = a - b 
    else: 
        if numero_2 == 0:
         print("operacion indefinida")
        else: 
            resultado = a / b 
    print (f"el resultado de {a}{op}{b} = {resultado}")
#ejecutar la funcion 
calculadora(numero_1, numero_2, operacion)

#ejercicio 4 
lado = float(input("ingrese la medida de su lado"))

def area_cuadrado(a):
    print(f"el area de su cuadrado {a} = {a*a}")
    