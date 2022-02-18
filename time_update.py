
"""
Created on Mon Feb 14 20:14:18 2022

@author: xu
"""


import os
import pandas as pd
import time
from datetime import datetime

start = time.clock()
#openpart
os.chdir('/home/xu/桌面/Nuess/0201/')

n=5 #the ship we choose to calculate the time
names = locals()

for k in range(n):
    names['neussboat' + str(k)] = pd.read_csv('neussboat_' + str(k) +'_time'+ '.csv')
    names['list' + str(k)] = names['neussboat' + str(k)].columns.tolist()

for k in range(n):
    j=0
    while j <len(names['list' + str(k)]):
        names['list' + str(k)][j]=names['list' + str(k)][j][11:19]
        j=j+1
        
for k in range(n):
    i=0
    names['list2_' + str(k)]=[]
    while i < (len(names['list' + str(k)])-1):
        Time_start=names['list' + str(k)][i]
        Time_end=names['list' + str(k)][i+1]   
        p2=datetime.strptime(str(Time_end),"%H:%M:%S")
        p1=datetime.strptime(str(Time_start),"%H:%M:%S")
        m=(p2-p1).seconds
        names['list2_' + str(k)].append(m)
        i=i+1
    time_update = pd.DataFrame([names['list2_' + str(k)]])
    time_update.to_csv('neussboat_' + str(k) +'_updatetime'+ '.csv',header = None,index=False)

end = time.clock()
print(end-start)

##avoid the overlength data 
#
##del list1[len(list1)-1]
#
#for i in range(len(list1)-1):
#    Time_start=list1[i]
#    Time_end=list1[i+1]   
#    p2=datetime.strptime(str(Time_end),"%Y-%m-%d %H:%M:%S")
#    p1=datetime.strptime(str(Time_start),"%Y-%m-%d %H:%M:%S")
#    m=(p2-p1).seconds
#    list2.append(m)
#x_axis= pd.DataFrame([list2])
#x_axis.to_csv('update_time.csv',header = None,index=False)