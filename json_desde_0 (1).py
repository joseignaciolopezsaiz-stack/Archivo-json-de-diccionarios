import json
data = {}  
def usuario():   
    file_name = "users_data.json"
    #cargar archivo json completo
    #print(data)
    a = len(data)
    #print(a)
    a = str(a+1)
    b = 'emp'+a
# Agregar una nueva entrada
    nombre = input("nombre: ")
    edad = input("edad: ")
    salario = input("salario: ")
    data[b] = {'nombre': nombre, 'edad': edad,"salario":salario}
    with open(file_name, "w") as f:
        json.dump(data,f, indent=4)
    with open(file_name,"r") as f:
        print(json.load(f))
        
n = int(input("numero de entradas: "))
for i in range(n):
    usuario()

