import pandas as pd

#cargar datos para analizarlos

#1. declarar una variable donde almaceno la fuente de datos

fuenteDatos = pd.read_csv("./empleados.csv")

#2. Obtener n cantidad de datos (filtro)
filtroHead = fuenteDatos.head() #primeros 5
print(filtroHead)

filtroHead2 = fuenteDatos.head(15) #primeros 15
print("\n")
print(filtroHead2)

print("\n")

filtroTail = fuenteDatos.tail() #último 5 datos
print(filtroTail)
print("\n")
ultimos30 = fuenteDatos.tail(30)
print(ultimos30)

#Acceder a una clave. En este caso imprimirá los 10 primeros nombres
filtroNombre = fuenteDatos.head(10)["nombres"]
print("\n")
print(filtroNombre)

print("\n")

#filtro Iloc
filtroIloc = fuenteDatos.iloc[5:15] # fila 5 a la 15
print("\n")
print(filtroIloc)
print("\n")
filtroIloc2 = fuenteDatos.iloc[[5,15]] #solo imprimirá la fila 5 y la 15
print(filtroIloc2)

print("\n")
#primeros 50 con salario
primeros50 = fuenteDatos.head(50)["salario"]
print(primeros50)

print("\n")
#obtener la información general de los 500 registros encontrando la media  aritmética o promedio de salarios 
media = fuenteDatos.describe()
print(media)
print("\n")
#Datos del registro 100, 200, 300, 400
filtros = fuenteDatos.iloc[[100,200,300,400]]
print(filtros)
print("\n")
#últimos 3 empleados. Solo quiero ver el nombre y el salario
nom_sal = fuenteDatos.tail(3)[["nombres","salario"]]
print(nom_sal)