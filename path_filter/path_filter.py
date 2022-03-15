# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:22:19 2022

@author: xu
"""

import os
from matplotlib import pyplot as plt
import pandas as pd

os.chdir('C:/sasy/Boat_neuss_0201/')#path
neuss_csv = pd.read_csv("neu_0201_1.csv")
neuss = pd.read_csv("neu_0201.csv")
#for next step, avoid to delete the neuss
#print(neuss.sample(10))
#a=neuss["randomid"]
ship_id = neuss_csv.drop_duplicates(subset=["randomid"], keep="first", inplace=False)#find all ship ids
ship_id1 = ship_id["randomid"]
ship_id_list = ship_id1.values.tolist()

wrong_ship_list=[]
fault_GPS_ship_id={}
names = locals()



for i in range(len(ship_id_list)):
    names[str(ship_id_list[i])] = neuss[(neuss["randomid"]==ship_id_list[i])]
    names[str(ship_id_list[i])] = names[str(ship_id_list[i])][["longitude"]].iloc[:, 0]
    names['longti' + str(ship_id_list[i])] = names[str(ship_id_list[i])].T
    names[str(ship_id_list[i])+'_list'] = names['longti' + str(ship_id_list[i])].values.tolist()
    
j=0    


while j < len(ship_id_list)-1:    
    for k in range((len(names[str(ship_id_list[j])+'_list'])-1)):
        if abs(names[str(ship_id_list[j])+'_list'][k]-names[str(ship_id_list[j])+'_list'][k+1]) >= 0.005:
            wrong_ship_list.append(ship_id_list[j])
    j=j+1


fault_GPS_ship_id = fault_GPS_ship_id.fromkeys(wrong_ship_list)#Removal of duplicate elements
wrong_ship_list = list(fault_GPS_ship_id.keys())

print(names[str(ship_id_list[j])+'_list'])
print(wrong_ship_list)

for m in range(len(wrong_ship_list)):
    index_names = neuss_csv[neuss_csv["randomid"]==wrong_ship_list[m]].index
    neuss_csv.drop(index_names, inplace = True)
    neuss_csv.to_csv('neu_0201_22.csv')
