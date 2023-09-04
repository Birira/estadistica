import pandas as pd
import seaborn as sns
import matplotlib as plt

data = pd.read_excel("auto.xlsx")

#coovarianza cov(X,Y)
#Si la Cov(X,Y) > 0 => la relacion es directa(mismo comportamiento, si baja una baja la otra, si sube una sube la otra)

#En caso contrario cov(X,Y) < 0 => la relacion es inversa

#Si cov(X,Y) = 0 => no existe relacion entre las variables


#matriz_cov = data[["price","mpg"]].cov() 
#print(matriz_cov)                                   #la relacion en este caso es inversa

#cov = matriz_cov.iloc[1,0]
#print(cov)

#coef de coorelacion
#-1<r<1
#si r es = 1, las variables son directamente proporcionales
#si r es =-1, las variables son inversamente proporcionales
#si r es = 0, no existe relacion entre las variables

#matriz_cor = data[["price","mpg"]].corr()
#print(matriz_cor)                               #existe una relacion inversa del 33,5% entre los datos

#sns.scatterplot(x = "mpg", y = "price",data=data)
sns.lmplot(x = "mpg", y = "price",data=data)
plt.show()