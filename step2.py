
"""
Created on Fri Feb 11 19:06:19 2022

@author: xu
"""


import os
import pandas as pd

os.chdir('/home/xu/桌面/Nuess/0201/')#path
neuss_csv = pd.read_csv("neu.csv")
neuss = pd.read_csv("neu.csv")
#for next step, avoid to delete the neuss
#print(neuss.sample(10))
#a=neuss["randomid"]
ship_id = neuss_csv.drop_duplicates(subset=["randomid"], keep="first", inplace=False)#find all ship ids
ship_id1 = ship_id["randomid"]
ship_id_list = ship_id1.values.tolist()

print(ship_id_list)
n=len(ship_id_list)
print(n)

names = locals()
for i in range(len(ship_id_list)):
    names['neussboat' + str(i)] = neuss[(neuss["randomid"]==ship_id_list[i])]
    names['neussboat' + str(i)].to_csv('neussboat' + str(i) + '.csv')
    
    names['longti' + str(i)] = names['neussboat' + str(i)][["longitude"]]
    names['longti' + str(i)] = names['longti' + str(i)].T
    names['longti' + str(i)].to_csv('neussboat_' + str(i) +'_long'+ '.csv',index=False,header = None)

    names['lati' + str(i)] = names['neussboat' + str(i)][["latitude"]]
    names['lati' + str(i)] = names['lati' + str(i)].T
    names['lati' + str(i)].to_csv('neussboat_' + str(i) +'_lati'+ '.csv', header = None,index=False)
    
    names['COG' + str(i)] = names['neussboat' + str(i)][["courseoverground"]]
    names['COG' + str(i)] = names['COG' + str(i)].T
    names['COG' + str(i)].to_csv('neussboat_' + str(i) +'_COG'+ '.csv', header = None,index=False)

    names['time' + str(i)] = names['neussboat' + str(i)][["timestamp"]]
    names['time' + str(i)] = names['time' + str(i)].T
    names['time' + str(i)].to_csv('neussboat_' + str(i) +'_time'+ '.csv', header = None,index=False)
    


#
#neussboat1 = neuss[(neuss["randomid"]==2060887)]
#neussboat1.to_csv('neuss1.csv')
#
#longti = neussboat1[["longitude"]]
#longti1= longti.T
#longti1.to_csv('neuss_boat_long.csv', header = None,index=False)
#
#lati = neussboat1[["latitude"]]
#lati1= lati.T
#lati1.to_csv('neuss_boat_lati.csv',header = None,index=False)
#
#cog = neussboat1[["courseoverground"]]
#cog1= cog.T
#cog1.to_csv('neuss_boat_cog.csv',header = None,index=False)
#
#time = neussboat1[["timestamp"]]
#time1= time.T
#time1.to_csv('neuss_boat_time.csv',header = None,index=False)