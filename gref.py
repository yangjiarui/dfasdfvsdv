#-*-coding:utf-8-*-
'''

@author:HANDSOME_JERRY
@time:'18-6-6下午9:23'
'''

import numpy as np
import matplotlib.pyplot as plt
class Node(object):
    def __init__(self,elem,up_num,down_num):
        self.elem=elem
        self.up_node=elem*up_num
        self.down_node=elem*down_num


class Interest_path(object):
    def __init__(self,initial,up_prob,down_prob):
        self.initial=initial
        self.up_prob=up_prob*initial
        self.down_prob=down_prob*initial



def sigmoid(x):
    return 1./(1+np.exp(-x))

class Tree(object):
    def __init__(self,layer):
        self.layer=layer
        self.root=None


    def generate(self,start,up_num,down_num,up_prob=1,down_prob=1,prob_start=1):
        node1=Node(start,up_num=up_num,down_num=down_num)
        node2=Interest_path(initial=prob_start,up_prob=up_prob,down_prob=down_prob)
        if self.root is None:
            self.root=node1
            self.root2=node2
        queue_class=[self.root]
        queue_class2=[self.root2]
        all={}

        all['price'],all['interest']=[],[]
        j=0
        #s=0
        #for z in range(self.layer):
        #    s+=2**z

        while queue_class and queue_class2:
            j+=1
            cur_int=queue_class2.pop(0)
            cur_node=queue_class.pop(0)
            cur_up_down={}
            ini={}
            res=[1]
           # adj=(sigmoid(np.sqrt(j))*np.random.normal(1))/np.sum(res)

            adj=sigmoid(np.sqrt(j/3600*24))/np.mean(res)
            res.append(adj)
            #adj=0
           # print('adj',adj)
            cur_up_down['up']=cur_node.up_node

            #adj / cur_node.elem +
            cur_up_down['expect_value']=(cur_int.up_prob*cur_node.up_node+cur_int.down_prob*cur_node.down_node)


            cur_up_down['down']=cur_node.down_node

            all['price'].append(cur_up_down)
            ini['ini_up']=cur_int.up_prob
            ini['ini_down']=cur_int.down_prob
            ini['ini_middle']=cur_int.initial
            all['interest'].append(ini)

            cur_node.up_node = Node(cur_node.up_node,up_num=up_num,down_num=down_num)
            cur_node.down_node = Node(cur_node.down_node,down_num=down_num,up_num=up_num)

            cur_int.up_prob=Interest_path(cur_int.up_prob,up_prob=up_prob,down_prob=down_prob)
            cur_int.down_prob=Interest_path(cur_int.down_prob,up_prob=up_prob,down_prob=down_prob)
            queue_class.append(cur_node.up_node)
            queue_class.append(cur_node.down_node)
            queue_class2.append(cur_int.up_prob)
            queue_class2.append(cur_int.down_prob)

            if j==2**(self.layer+1)-1:
                break
        a=all['price']
        b=all['interest']
        return a,a[2**(self.layer)-1:],b,b[2**(self.layer)-1:]


#if __name__=='__main__':

import time

a=1000
def Main(start):
    aaaa=[]

    full_raw=[]

    for w in range(start+1,start+5):
        #full_raw[str(start)+'-'+str(start+5)]=[]
        q=Tree(layer=w)
        int=0.6753233454
        q1 = time.time()
        full_nodes,last_layer,ful_ini,last_ini=q.generate(start=a,up_num=1.513383214,down_num=0.3362550236,up_prob=int,down_prob=1-int)

        expect=[last_layer[i]['expect_value'] for i in range(len(last_layer))]
        intin=[last_ini[f]['ini_middle'] for f in range(len(last_ini))]
        aaaa.append(np.mean(expect))
        full_raw.append(expect)
        print('time_used:', time.time() - q1)
        print('cur_inspection:',np.mean(expect))

    print('totol:',np.mean(aaaa))
   # print('%dto%d time_used:' % (start, start + 5), time.time() - q1)
    return start,np.mean(aaaa),full_raw,intin


import multiprocessing
pools=multiprocessing.Pool(processes=6)

result=[]
for v in range(0,5*6,5):

    result.append(pools.apply_async(Main,args=(v,)))

pools.close()
pools.join()

qqqq={}
full=[]
las_i=[]
for no in result:

    index,every_five_mean_value,every_five_full_value,last_ini=no.get()
    full.append(every_five_full_value)
    las_i.append(last_ini)
    qqqq[str(index)+'-'+str(index+5)]=every_five_mean_value



