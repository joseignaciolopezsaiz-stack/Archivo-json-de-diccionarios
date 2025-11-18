import json
#cargar archivo json completo
file_name = "users_data.json"
with open(file_name,"r") as f:
    data = json.load(f)
print(data)
#iterar sobre el diccionario
for user in data:
    print(user)
    file_name = f"user_{user}.json"
    with open(file_name, "w") as f:
        json.dump(data[user],f, indent=4)
        print(file_name, "saved successfully!")


# cargar  usuario 4
file_name = "user_emp4.json"
with open(file_name,"r") as f:
    print(json.load(f))
    print("----<<<ttt>>>----")
with open(file_name,"r") as f:
    print(f.read())
    print("-----<<<000>>>-----")