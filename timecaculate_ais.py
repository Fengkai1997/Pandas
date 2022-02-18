#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:43:38 2022

@author: xu
"""


import os
import pandas as pd
import time
from datetime import datetime
#openpart
os.chdir('/home/xu/桌面/1/')
pd_reader = pd.read_csv("duis_boat_time.csv")
#pd_reader1= pd_reader1.drop('columns',axis=0)
#pd_reader1= pd_reader.head(1)
#pd_reader1 = pd_reader.drop(labels=[1],axis=0)
list1 = pd_reader.columns.tolist()#dataframe2list
list2=[]

#avoid the overlength data 
for j in range(len(list1)):
    a=list1[j]
    list1[j]=a[0:19]
#del list1[len(list1)-1]

for i in range(len(list1)-1):
    Time_start=list1[i]
    Time_end=list1[i+1]   
    p2=datetime.strptime(str(Time_end),"%Y-%m-%d %H:%M:%S")
    p1=datetime.strptime(str(Time_start),"%Y-%m-%d %H:%M:%S")
    m=(p2-p1).seconds
    list2.append(m)
x_axis= pd.DataFrame([list2])
x_axis.to_csv('update_time.csv',header = None,index=False)


#for i in range(len(list1)-1):
#    Time_start=list1[i]
#    Time_end=list1[i+1]
#    Time_start_1 = time.strptime(Time_start,"%d-%b-%Y %H:%M:%S")
#    Time_start_2 = time.strftime("%d-%m-%Y %H:%M:%S",Time_start_1)
#    Time_end_1 = time.strptime(Time_end,"%d-%b-%Y %H:%M:%S")
#    Time_end_2 = time.strftime("%d-%m-%Y %H:%M:%S",Time_end_1)
#    p2=datetime.strptime(str(Time_end_2),"%d-%m-%Y %H:%M:%S")
#    p1=datetime.strptime(str(Time_start_2),"%d-%m-%Y %H:%M:%S")
#    m=(p2-p1).seconds
#    list2.append(m)
#    
#x_axis= pd.DataFrame([list2])
#x_axis.to_csv('update_time.csv')
