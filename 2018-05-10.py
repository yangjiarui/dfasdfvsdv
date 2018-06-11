# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os,sys
import statsmodels.api as sm
from glob import glob
#sys.setdefaultencoding('cp936')
#file_list=os.listdir('E:\iFind_data')
os.chdir('E:\iFind_data')
file_list=glob('*[0-9]*')
os.chdir('E:\iFind_data')
#f=open(file_list[0])
data=pd.DataFrame()
for i in file_list:
    df=pd.read_csv(i,encoding='cp936')
    df.index=df.iloc[:,2]
    df.index=pd.DatetimeIndex(df.index)
    df=df.drop('时间',axis=1).iloc[:-1,:]
    name=df.iloc[0,1]
    data[name]=df['收盘价']
    
#indexes
os.chdir('E:\指数类')
dir=os.listdir('E:\指数类')
zhishus=pd.DataFrame()

def normalize_data(dd,window):    ##dd:Series
    if np.isnan(dd[0]):
        dd=dd.fillna(dd.mean())
    else:
        w=[]
        for j in range(len(dd)):
            if np.isnan(dd[i]):
                w.append[-abs(window):]
            else:
                w.append(dd[i])
        return pd.Series(w,index=dd.index)

def make_lstls(df,data):     #df:Serise  data:DataFrame
    df=np.log(df/df.shift(1))
    data=np.log(data/data.shift(1))
    
    df=df.fillna(df.mean())    #normalize_data(dd=df,window=10)
#    dat=pd.DataFrame()
#    for i in data.columns:
#        dat[i]=normalize_data(data[i],window=5)
    data=data.fillna(data.mean())
    
    
    
    min_raw=min(len(df),len(data))
    df,data=df[:min_raw],data[:min_raw]
    
    model=sm.OLS(df.values,sm.add_constant(data.values)).fit()
    #model.fit()
    return model


aic={}
for j in dir:
    ds=pd.read_csv(j,encoding='cp936')
    ds.index=ds['时间']
    ds.index=pd.DatetimeIndex(ds.index)
    ds=ds.drop('时间',axis=1).iloc[:-1,:]
    name_index=ds.iloc[0,1]
    #zhishus[name]=ds['收盘价']
    new=[]
    for n in ds.iloc[:,5]:
        cur_nod=n.split(',')
        node=cur_nod[0]
        for k in range(1,len(cur_nod),1):
            node+=cur_nod[k]
        new.append(float(node))
    dev=pd.Series(new,index=ds.index)
    
    cur=make_lstls(df=dev,data=data)
    print(str(name_index)+'最小二乘2data结果是:\n')
    print(cur.summary())
    #c_aic=cur.aic
    aic[name_index+'aic:']=cur.aic
    #aic=min_aic
    #if min_aic<cur.aic:
    #    aic=min_aic
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    