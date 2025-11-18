#import requests
import json

data = {
    "emp1": {"name": "Lisa", "age": 34, "salary": 54000},
    "emp2": {"name": "Elis", "age": 24, "salary": 40000},
    "emp3":{"name":"Piter","age":41,
"salary":43200},
    "emp4":{"name":"Ilenia","age":41,
"salary":43800},
}
# save all data in a single JSON file
file_name = "users_data.json"
with open(file_name, "w") as f:
    json.dump(data, f, indent=4)
    print(file_name, "saved successfully!")
# or you can save each entry into a file
#o puedes guardar cada entrada en un archivo
#iterar sobre el diccionario
for user in data:
    print(user)
    file_name = f"user_{user}.json"
    with open(file_name, "w") as f:
        json.dump(data[user],f, indent=4)
        print(file_name, "saved successfully!")


# cargar segundo usuario
file_name = "user_emp4.json"
with open(file_name,"r") as f:
    print(json.load(f))
    print("----<<<ttt>>>----")
with open(file_name,"r") as f:
    print(f.read())
    print("-----<<<000>>>-----")