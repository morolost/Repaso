import os
os.system("cls")

x= [42, 3.14, "Hola", True]

for i, v in enumerate(x):
    print(f"Índice: {i}, Valor: {v}, Tipo: {type(v)}")
    
os.system("pause")