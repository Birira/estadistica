import csv
import pandas as pd
x1 = []

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
#titan.set_index(titan["PassengerId"], inplace=True)

#iloc sirve para buscar por el indice original, osea apartir del 0
#loc sirve para trabajar con el indice antes seteado
#print(titan.iloc[355])
#print("#################")
#print(titan.loc[355,["Name","Age"]])


#*****titan[titan["PassengerId"],]
#print(titan.sort_values(by=["Name"],ascending=True))
#print(titan.sort_values(by=["Name"],ascending=True).loc[:,["Name","Age"]])



#################
#encuentre la cantidad de sobrevivientes de la clase 1

total = titan.apply(lambda x: (x["Pclass"] == 1)&(x["Survived"]), axis=1).sum()
print(total)