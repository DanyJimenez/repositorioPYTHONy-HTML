# creando diccionarios en Python

persona = {
    "nombre": "Dany",
    "edad": 30,
    "estatura": 1.80,
    "yaDesayuno": False,
    "equiposFavoritos": ["Nacional", "Arsenal", "Boca"]
}

#creando un diccionario vacío

ciudad = {}

#accedamos a un diccionario

print(persona)
print(ciudad)

#acceder a un solo atributo o clave del diccionario

nombre = persona["nombre"]
print(nombre)
print(persona["nombre"])
persona["nombre"] = "Ana"
print(persona["nombre"])
print(persona)

persona["saldoEnCuenta"] = 0
print(persona["saldoEnCuenta"])

print(persona.get("equiposFavoritos")) #otra manera de acceder un atributo

#recorriendo un diccionario
for atributo in (persona.values()):
    print(atributo)

