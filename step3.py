#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:48:55 2022

@author: xu
"""


import os
import pandas as pd
import time
#
#start = time.clock()
os.chdir('/home/xu/桌面/Nuess/0201/')#path
pd_reader1 = pd.read_csv("0201.csv")#file_name
pd_reader = pd_reader1[["randomid", "timestamp", "longitude","latitude","courseoverground","km"]]#choose the columns
pd_reader.to_csv('0201.csv')


time=pd_reader.pop("timestamp") 
time1=time.str[11:13]
pd_reader.insert(6,'time_24h',time1)
#a=time1[80000*2]

#choose the areas and input in files
#neuss = pd_reader[(pd_reader["km"]>777)&(pd_reader["km"]<784)]
#neuss.to_csv('neuss.csv')

#end = time.clock()
#print(end-start)