#Clase 21-08-23
#Trabaja con auto.xlsx y la libreria seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel('auto.xlsx')

plt.figure(figsize=(8,6))
data = data[data["grupo"]==1]
data.dropna(inplace=True)


#sns.histplot(data=data, x="car brands")
#plt.show()

#sns.histplot(data=data, x="price",kde=True)
#plt.show()

#sns.displot(data=data, x ="price", row="car brands",kde=True)
#plt.show()

#sns.boxenplot(data=data, y="price", x = "car brands")
#plt.show()

agrupar = data.groupby("car brands").size()

marcas = ["audi","bmw","ford","volkswagen"]
frecuencias = [1048,1062,1808,1473]

plt.pie(frecuencias, labels=marcas, autopct='%1.1f%%')
plt.show()