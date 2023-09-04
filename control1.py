import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

#uso de advertising.csv
data = pd.read_csv("Advertising.csv",sep = ",")

prom_np = np.mean(data["TV"])
mediana = np.median(data["TV"])
moda = stats.mode(data=data["TV"])

print("promedio TV: ",prom_np)
print("mediana TV: ",mediana)
print("moda TV: ",moda)

print("################################################################")

p80tv = np.percentile(data["TV"],80)
p80radio = np.percentile(data["Radio"],80)
p80otra = np.percentile(data["Newspaper"],80)
p80tv = round(p80tv,2)
print("percentil 80tv: ", p80tv)
print("percentil 80radio: ", p80radio)
print("percentil 80newspaper: ", p80otra)

print("################################################################")

promedio_newspaper = np.mean(data["Newspaper"])
varianza_ddof1 = np.var(data["Newspaper"], ddof = 1)
desv_std1 = np.sqrt(varianza_ddof1)
CV_01 = (desv_std1/promedio_newspaper)
print("coef newspaper: ", CV_01)