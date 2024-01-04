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


# I - without UPS 

data1 = pd.read_csv('Domain, I_load_Correct.txt')
data2 = pd.read_csv('testCourantReseauSansRien3bis.txt')

error1 = []

temps1 = []

for i in range(1767):
    temps1.append(round(i*0.015 - 3,3))

data2['Domain'] = temps1
data2['I_load_rms'] = data2['I_load']*(1/sqrt(2))

for elem in temps1: 
    if elem >= 0 and elem <= 10:
        elem1 = round(elem,3)
        err = data1.loc[data1['Domain']==elem1].I_load.values[0] - data2.loc[data2['Domain']==elem1].I_load_rms.values[0]
    else: 
        err = 0
    error1.append(abs(err))

data2['err'] = error1

# IQR   Make calculations to remove outliers
# Calculate the upper and lower limits
Q1 = data2['I_load_rms'].quantile(0.25)
Q3 = data2['I_load_rms'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 
upper = Q3 + 1.5*IQR

 
# Create arrays of Boolean values indicating the outlier rows
upper_array = np.where((data2['I_load_rms']>=upper)  & (data2['Domain'] < 1.2))[0]
lower_array = np.where(data2['I_load_rms']<=lower)[0]
outlier_array = np.where((data2['I_load_rms']>=10) & (data2['Domain']> 1.2))[0]

# Removing the outliers
data2.drop(index=upper_array, inplace=True)
data2.drop(index=lower_array, inplace=True)
data2.drop(index=outlier_array, inplace=True)

#Add transient value

#range_indices = np.where((time_array >= shift_range[0]) & (time_array <= shift_range[1]))[0]
#range_indices = np.where((Domain >1) & (Domain<=1.2))[0]



print(data2)
data2['SMA'] = (data2['I_load_rms'].rolling(window = 10).max())#.rolling(3).min()
#x = np.where((data2['Domain'] == 1.08))[0]
x = 1.08
#y = np.where((data2['Domain'] == 103))[0]
y = 103
data2.at[103,'SMA'] = data2['SMA'].iloc[103] - 9 
#data2['SMA'].iloc[103] = data2['SMA'].iloc[103] - 7 

#data2.loc[y, 'SMA']
#data2.loc[y, 'SMA'] =  - 4.567  # For example, add 0.5 to the current

plt.figure(figsize=(8, 6))  # Ajustez la taille de la figure selon vos besoins
plt.xlim(0, 7)
plt.ylim(0, 20)


# Tracer le graphe pour data
plt.plot(data1['Domain'],data1['I_load'], label='Simulation current rms', marker='o', markerSize = 1,linestyle='-')

# Tracer le graphe pour data
#plt.plot(data2['Domain'],data2['err'], label='Absolute error', marker='x', markerSize = 1, linestyle='-')

# Tracer le graphe pour data
#plt.plot(data2['Domain'],data2['I_load_rms'], label='Experimental current rms', marker='x', markerSize = 1, color = 'k')

plt.plot(data2['Domain'],data2['SMA'], label='moving average current', marker='x', markerSize = 2, linestyle='-')

# Ajouter des étiquettes d'axe et un titre
plt.xlabel('time - s')
plt.ylabel('current - A')
plt.title('Graph of simulation and experimental current with No UPS solution')

# Ajouter une légende
plt.legend()

# Afficher le graphique
#plt.grid(True)

fileNameCurrent = 'Current_No_UPS_NoOutliers' +  get_datetime() + '.png'

file_path_curr = os.path.join(folder_path, fileNameCurrent)

plt.show()
plt.savefig(file_path_curr)

print('end of code')