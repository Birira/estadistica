#clase 1, 11-08, repaso de pyhton con estadistica descriptiva
import numpy as np
import statistics as stats

#VARIABLES
estaturas = [176.5, 163.8, 182.3, 153.1, 175.6, 153.1, 170.0]
suma = 0

#MEDIDAS DE TENDENCIA CENTRAL
#forma normal para sacar promedio
for i in range(len(estaturas)):
    suma += estaturas[i]

promedio = suma/len(estaturas)
#print(promedio)

#usando numpy
prom_np = np.mean(estaturas)
#print(round(prom_np,2))

#sacar mediana
mediana = np.median(estaturas)
#print(mediana)

#para el caso de la moda, se usa statistics
moda = stats.mode(data=estaturas)
#print(moda)


#MEDIDAS DE POSICION
#percentiles
p25 = np.percentile(estaturas,25)
#print(p25)

#cuartiles
Q1 = stats.quantiles(data=estaturas, n=2)
#print(Q1)

#MEDIDAS DE DISPERSION
#varianza
varianza_ddof0 = np.var(estaturas, ddof = 0) #ddof = 0 para poblaciones, ddof = 1 para muestras
varianza_ddof1 = np.var(estaturas, ddof = 1)
print(varianza_ddof0)
print(varianza_ddof1)

#desviacion estandar
desv_std0 = np.sqrt(varianza_ddof0)
desv_std1 = np.sqrt(varianza_ddof1)
#print(desv_std0)
#print(desv_std1)

#coeficiente de variacion
CV_00 = (desv_std0/promedio)*100
CV_01 = (desv_std1/promedio)*100
print(CV_00)
print(CV_01)