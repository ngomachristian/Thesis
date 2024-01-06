import matplotlib.pyplot as plt
import pandas as pd
from math import *
import random
from datetime import timedelta, datetime, tzinfo, timezone
import os
import numpy as np 
# Functions

def get_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    return formatted_datetime

folder_path = 'images'
os.makedirs(folder_path, exist_ok=True)

print('code has started')


# V with UPS
data1 = pd.read_csv('Domain-Vload_solution_UPS.txt')
data2 = pd.read_csv('testTensionReseauSortieUPS1Corrected.txt')

error1 = []

temps1 = []

for i in range(624):
    temps1.append(round(i*0.015 - 3,3))

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


# IQR   Make calculations to remove outliers
# Calculate the upper and lower limits
Q1 = data2['V_load'].quantile(0.25)
Q3 = data2['V_load'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 
upper = Q3 + 1.5*IQR

 
# Create arrays of Boolean values indicating the outlier rows#
outlier_array = np.where((data2['V_load']>=upper) & (data2['Domain']> 1.2))[0]
upper_array = np.where((data2['V_load']>=upper)  & (data2['Domain'] <= 1.2))[0]
lower_array = np.where(data2['V_load']<=lower)[0]

# Removing the outliers
#data2.drop(index=upper_array, inplace=True)
#data2.drop(index=lower_array, inplace=True)
#data2.drop(index=outlier_array, inplace=True)

data2['err_avg'] = data2['err'].rolling(5).max().rolling(3).min()
data2['SMA'] = (data2['V_load_rms'].rolling(5).max()).rolling(3).min()

plt.figure(figsize=(8, 6))  # Ajustez la taille de la figure selon vos besoins
plt.xlim(0, 5)
plt.ylim(0,280 )

# Tracer le graphe pour data
plt.plot(data2['Domain'],data2['V_load_rms'], label='Experimental voltage', marker='x', markerSize = 1)

# Tracer le graphe pour data
plt.plot(data1['Domain'],data1['V_load'], label='Simulation voltage', marker='o', markerSize = 1,linestyle='-')

# Tracer le graphe pour data
#plt.plot(data2['Domain'],data2['err_avg'], label='Absolute error', marker='x', markerSize = 1, linestyle='-', color = 'k')

#plt.plot(data2['Domain'],data2['SMA'], label='moving average voltage', marker='x', markerSize = 2, linestyle='-')

# Ajouter des étiquettes d'axe et un titre
plt.xlabel('time - s')
plt.ylabel('Voltage - V')
plt.title('Graph of simulation and experimental voltage without UPS solution')

# Ajouter une légende
plt.legend()

# Afficher le graphique
#plt.grid(True)

fileNameCurrent = 'Voltage_UPS' +  get_datetime() + '.png'

file_path_curr = os.path.join(folder_path, fileNameCurrent)

plt.savefig(file_path_curr)

plt.show()

### Calculate voltage ###


print('end of code')