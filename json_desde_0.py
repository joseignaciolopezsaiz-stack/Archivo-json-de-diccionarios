import json

file_name = "users_data.json"
data = {}
with open(file_name, "w") as f:
    json.dump(data,f, indent=4)
    
def usuario():   
    file_name = "users_data.json"
    #cargar archivo json completo
    
    with open(file_name,"r") as f:
        data = json.load(f)
    print(data)
    a = len(data)
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
usuario()
usuario()
usuario()
usuario()

