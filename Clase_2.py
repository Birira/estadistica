#Manipular archivo csv titanic


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#manipular un archivo, sep para las separaciones de las celdas
titan = pd.read_csv("titanic.csv",sep=";")
#head imprime los primeros datos, en este caso los primeros 5
#print(titan.head(5))
#el contrario de head, enterga los finales
#print(titan.tail(7))


#informacion del archivo 
#print(titan.info())
#print(titan.describe())
#print(titan["Age"].describe())
#print(titan.columns)
#print(titan.index)

#setear un indice
titan.set_index(titan["PassengerId"], inplace=True)

#iloc sirve para buscar por el indice original, osea apartir del 0
#loc sirve para trabajar con el indice antes seteado
#print(titan.iloc[355])
#print("#################")
#print(titan.loc[355,["Name","Age"]])


#print(titan[titan["PassengerId"]%3==0])
#print(titan.sort_values(by=["Name"],ascending=True))
#print(titan.sort_values(by=["Name"],ascending=True).loc[:,["Name","Age"]])



#################
#encuentre la cantidad de sobrevivientes de la clase 1

#total = titan.apply(lambda x: (x["Pclass"] == 1)&(x["Survived"]), axis=1).sum()
#print(total)

#age_filter = titan[titan["Age"].notna()]                       #filtro de pasajeros con edad N/A
#print(age_filter)

#age_filter["adulto"] = np.where(age_filter["Age"] >= 18,1,0)   #filtro de mayores de edad
#print(age_filter["adulto"])

#matplotlib

x = np.linspace(0,7,500)    #dominio
y = np.sin(x)               #funcion
plt.figure(figsize=(6,8))
plt.axhline(0,color = "black")
plt.axvline(0,color = "black")
plt.plot(x,y)
plt.show()
