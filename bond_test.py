# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:56:51 2018

@author: 834235185
"""

import numpy as np
df=np.zeros((322100000,1))
bond=np.zeros((322100000,1))
bond[:]=np.nan
df[:]=np.nan
df[0]=0.045
bond[0]=100

class Node(object):
    def __init__(self,i,df):
        if df[i] == np.nan:
            print('find an NAN')
            return
        self.root=df[i]
        self.up=self.root*1.111111111
        self.down=self.root*0.999999999
        self.i=i
        self.df=df
    def get_up(self):
        
        df[2*self.i+1]=self.up
        return self.up
    
    def get_down(self):
        df[2*self.i+2]=self.down
        return self.down
    
    
    
    
root=[]
up=[]
down=[]
s=0
for z in range(27):
    s=s+2**z
print('Done',s)
for j in range(134217727):
    root.append(df[j])
    cur=Node(df=df,i=j)
    down.append(cur.get_down())
    up.append(cur.get_up())
    
y=df[np.isnan(df)==False]
import pandas as pd
import matplotlib.pyplot as plt
used=y[2**27:]

fig=plt.figure()
ax=fig.add_subplot(111)

ax.hist(used,bins=60)
ax.set_xticks(np.linspace(0,0.7,20))

plt.show()

#class calculate_node_price(object):
#     def __init__(self,bond_node_index,bond,sigma,pre_up_mean=0,pre_down_mean=0):
#         self.bond_node_value=bond[bond_node_index]
#         self.bond=bond
#         self.bond_node_index=bond_node_index
#         self.sigma=sigma
#         qq=np.random.randn(2)
#         self.up_prob=float(qq[0]/sum(qq))
#         self.down_prob=float(qq[1]/sum(qq))
#         self.int=np.mean(interest[2*self.bond_node_index+1]+interest[2*self.bond_node_index+2])
#         self.cur=self.bond_node_value
#         self.pre_up_mean=pre_up_mean
#         self.pre_down_mean=pre_down_mean
#     def get_up_bonf_price(self):
#         print('up',0.2*self.pre_up_mean+0.8*(1+1.11111111111*self.int)*self.bond_node_value*abs(self.up_prob)*np.exp(2*self.sigma))
#         bond[2*self.bond_node_index+1]=0.2*self.pre_up_mean+0.8*(1+1.11111111111*self.int)*self.bond_node_value*abs(self.up_prob)*np.exp(2*self.sigma)
#         return 0.2*self.pre_up_mean+0.8*(1+1.11111111111*self.int)*self.bond_node_value*abs(self.up_prob)*np.exp(2*self.sigma)
#     def get_down_bonf_price(self):
#         print('down',(1+0.9999999999999*self.int)*self.cur*abs(self.down_prob)*np.exp(2*(-self.sigma)))
#         bond[2*self.bond_node_index+2]=0.2*self.pre_down_mean+0.8*(1+0.999999999999*self.int)*self.bond_node_value*abs(self.down_prob)*np.exp(2*(-self.sigma))
#         return 0.2*self.pre_down_mean+0.8*(1+0.999999999999*self.int)*self.bond_node_value*abs(self.down_prob)*np.exp(2*(-self.sigma))
#    
#r=Node(df=df,i=0)
#
#a,b,c=[],[],[]
#up,down=[],[]
#up.append(0)
#down.append(0)
#for q in range(5000000):
#    s=np.random.rand(1)/10
#   
#    qq=calculate_node_price(bond_node_index=q,bond=bond,sigma=np.sqrt(q)*s,pre_up_mean=up[-1],pre_down_mean=down[-1])
#    qq.get_down_bonf_price()
#    qq.get_down_bonf_price()
#    a.append(bond[q].tolist())
#    b.append(qq.get_down_bonf_price().tolist())
#    c.append(qq.get_up_bonf_price().tolist())
#    up.append(np.mean(c))
#    down.append(np.mean(b))
#w=bond[np.isnan(bond)==False]
#print(len(w))