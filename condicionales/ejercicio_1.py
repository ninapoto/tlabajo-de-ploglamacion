# crear un pograma que convierta unidades de temperatura.
#1.- el usuario debera ingresar el valor de t°
#2.- el usuario debera ingresar escala de t° original.
#3.- el usuario debera ingresar escala de t° final.
#4.- el sistema debera entregar resultados d conversion. 

# de °C a °K => °C + 273.15
# de °K a c° => °K - 273.15

# de °C a °F => (°C * 9/5) + 32 
# de °f a °C => (°F - 32) * 5/9

# de °F a °K => (°F -32) * 5/9 + 273.15
# de °K a °F => ((°K - 273.15)* 9/5) + 32
   


   def convertidor_temp(temperatura, inicio, fin):
    resultado = 0 

    if inicio == "C":
        if fin == "K":
            
        elif fin == "F":
            pass
        else:
             print ("escala final erronea")
    elif inicio == "C":
        if fin == "K":
            pass
        else:
             print("Escala final erronea")
    elif inicio == "F": 
        if fin == "k":
            pass
        elif fin == "F":
        else :
            print("escala final erronea")

    print