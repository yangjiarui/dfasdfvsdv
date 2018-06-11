# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:36:22 2018

@author: 834235185
"""

import itchat,time,os,jieba
import pandas as pd
import numpy as np
itchat.auto_login(enableCmdQR=False,hotReload=False)
friends=itchat.get_friends()
mps=itchat.get_mps()
mpslist=[]
all=[]
for i,mp in zip(friends,mps):
    cur1,cur2={},{}
    cur1['个签']=i['Signature']
    cur1['昵称']=i['NickName']
    cur1['此次地址']=i['UserName']
    cur2['个签']=mp['Signature']
    cur2['昵称']=mp['NickName']
    cur2['此次地址']=mp['UserName']
    all.append(cur1)
    mpslist.append(cur2)
    
os.chdir('E:\迅雷下载')
for j in all:
    if '平安保险' in j['昵称']:      #'Al':
        w=0
        print('Find')
        with open('乡村艳妇.txt','r',encoding='utf-8') as f:
            mse2=[]
            for line in f.readlines():
                nnn=line.strip()
                #print(nnn)
                if nnn != '':
                    ee=jieba.cut(nnn)
                    fin=' '.join(ee).split(' ')
                    mse2.append(fin)
                
                
                
                
#                
#for j in mpslist:
#    if '人人宽客' in j['昵称']:      #'Al':
#        w=0
#        with open('乡村艳妇.txt','r',encoding='utf-8') as f:
#            mse2=[]
#            for line in f.readlines():
#                nnn=line.strip()
#                #print(nnn)
#                if nnn != '':
#                    ee=jieba.cut(nnn)
#                    fin=' '.join(ee).split(' ')
#                    mse2.append(fin)
                
                
        w=0
        while True:
            
            mse=['叫你不理我','哈哈','呵呵','这是什么','女神','接哦']
           
            w+=1
            itchat.send_msg('猜猜我要发几条信息给你:('+str(np.random.randn(1)[0])+')  '+mse[0]+'_'+np.random.choice(mse2[np.random.choice(range(len(mse2)))])+'干!',toUserName='@eae3ccbceb5126ad014f94677662eaba')
            time.sleep(1+w*2)
            print(str(w)+'has send')
            
            if w%100==0:
                x=input('是否继续')
                if int(x)==1:
                    continue
                else:
                    
                    itchat.send_msg('实在不好意思，上述信息是用python发给你的恶作剧，并不是你的微信问题，请多包含',toUserName='@eae3ccbceb5126ad014f94677662eaba')
                    break
        print('Done')
        itchat.logout()