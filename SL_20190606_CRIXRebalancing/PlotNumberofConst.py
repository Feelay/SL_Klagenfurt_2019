# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:13:44 2019

@author: Patrick Plum

Description: This script plots the number of CRIX constituents over time
- called by: CRIXRebalancingMaster.py - pls run the latter
"""

############################### Import Modules #############################################

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from __main__ import dates_of_ind_rebalance
from __main__ import dates_of_first
from __main__ import crix_constituents


##################### Amount of currencies at a certain time preiod ########################

#amount of currencies in each period
n = []
for i in dates_of_first:
    n.append(len(crix_constituents.loc[i]))

#plotting number of constituents over time
fig=plt.figure(figsize=(12,3))
axes=fig.add_axes([0.1,0.1,0.8,0.8])
x=dates_of_first
y=n
axes.plot(x,y,'g+',mew=3,ms=10)
plt.xticks(dates_of_ind_rebalance)
myFmt = mdates.DateFormatter('%Y-%m-%d')
axes.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
plt.savefig('Nr_of_Cryptos.png')

############################################################################################
