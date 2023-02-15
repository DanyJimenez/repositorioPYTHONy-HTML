import pandas as pd

data = pd.read_csv('./empleados.csv')

header = data.head()
#print(header)

print('\n')

analistasBajoCosto = data[(data["salario"]<5000000)&(data["cargo"]=="analista1")].head(20)
print(analistasBajoCosto.head(20))


print('\n')
#exportando un data frame a html

archivoHTML = analistasBajoCosto.to_html()
archivo = open("bajoCosto.html", "w")
archivo.write(archivoHTML)
archivo.close()

