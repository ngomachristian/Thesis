import matplotlib.pyplot as plt
import pandas as pd
from math import *
import random
from datetime import timedelta, datetime, tzinfo, timezone
import os

#from file_path_curr import file_path_curr

# Functions

def get_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    return formatted_datetime

folder_path = 'images'
os.makedirs(folder_path, exist_ok=True)

print('code has started')


# V without UPS
data1 = pd.read_csv('Domain, Vload-Correct.txt')
data2 = pd.read_csv('testTensionReseauSansRien1.txt')

error1 = []

temps1 = []

for i in range(1250):
    temps1.append(round(i*0.015 -1.50, 3))


data2['Domain'] = temps1
data2['V_load_rms'] = data2['V_load']

for elem in temps1: 
    if elem >= 0 and elem <= 10:
        elem1 = round(elem,3)
        err = data1.loc[data1['Domain']==elem1].V_load.values[0] - data2.loc[data2['Domain']==elem1].V_load_rms.values[0]
    else: 
        err = 0
    error1.append(abs(err))

data2['err'] = error1
data2['err_avg'] = data2['err'].rolling(5).max().rolling(3).min()
data2['SMA'] = (data2.drop(0)['V_load_rms'].rolling(5).max()).rolling(3).min()

plt.figure(figsize=(8, 6))  # Ajustez la taille de la figure selon vos besoins
plt.xlim(0, 10)
plt.ylim(0, 350)

# Tracer le graphe pour data
#plt.plot(data2['Domain'],data2['V_load_rms'], label='Experimental voltage', marker='x', markerSize = 2)

# Tracer le graphe pour data
#plt.plot(data1['Domain'],data1['V_load'], label='Simulation voltage rms', marker='o', markerSize = 2,linestyle='-')

# Tracer le graphe pour data
plt.plot(data2['Domain'],data2['err_avg'], label='Absolute error', marker='x', markerSize = 2, linestyle='-')

#plt.plot(data2['Domain'],data2['SMA'], label='experimental voltage rms', marker='x', markerSize = 2, linestyle='-')

# Ajouter des étiquettes d'axe et un titre
plt.xlabel('time - s')
plt.ylabel('Voltage - V')
plt.title('Graph of simulation and experimental voltage without UPS solution')

# Ajouter une légende
plt.legend()

# Afficher le graphique
#plt.grid(True)

fileNameCurrent = 'Voltage_No_UPS' +  get_datetime() + '.png'

plt.savefig(fileNameCurrent)

plt.show()

### Calculate voltage ###


print('end of code')