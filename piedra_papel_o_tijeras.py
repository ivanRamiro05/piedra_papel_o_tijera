# piedra papel o tijeras
print("----------------------------------")
print("-------------A--JUGAR-------------")
print("----------------------------------")
#INPUT
import random
op = ["piedra", "papel", "tijeras"]

#PROCESSING
while True:
    usuario=input("elija piedra, papel o tijeras: ")
    if usuario not in op:
        print("movimiento no valido")
        continue 
    pc=random.choice(op)
    print(f"\n La pc a seleccionado {pc} ") 
    if usuario == pc:
        print ("\nEmpate!, ambos eligieron",{pc}) 
    elif usuario== "piedra" and pc == "tijeras":
        print("\nGanaste!, {usuario} gana en contra de {pc}")
    elif usuario== "tijeras" and pc == "papel":
        print("\nGanaste!, {usuario} gana en contra de {pc}")
    elif usuario== "palpel" and pc == "piedra":
        print("\nGanaste!, {usuario} gana en contra de {pc}")
    else:
        print("\nPerdiste!, {usuario} pierde en contra de {pc}")
        
#Fin
