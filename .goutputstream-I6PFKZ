#-*-coding:utf-8-*-
'''

@author:HANDSOME_JERRY
@time:'18-6-5下午9:15'
'''
import numpy as np
import matplotlib.pyplot as plt
class Node(object):
    def __init__(self,elem,last_prob,up_num,down_num,up_prob,down_prob):
        self.elem=elem
        self.last_prob=last_prob
        self.up_node=elem*up_num
        self.down_node=elem*down_num
        self.up_prob=up_prob*last_prob
        self.down_prob=down_prob*last_prob


def sigmoid(x):
    return 1./(1+np.exp(-x))

class Tree(object):
    def __init__(self,layer):
        self.layer=layer
        self.root1=None
       # self.root2=None

    def generate(self,start,last_prob=1,up_num,down_num,up_prob=1,down_prob=1):
        node=Node(start,last_prob, up_num=up_num,down_num=down_num,up_prob=up_prob,down_prob=down_prob)

        if self.root1 is None:
            self.root1=node
       # if self.root2 is None:
      #      self.root2=node
        queue_class1=[self.root1]
       # queue_class2=[self.root2]
        all={}
        a=[]
        all['up'],all['down']=[],[]
        j=0
        #s=0
        #for z in range(self.layer):
        #    s+=2**z

        while queue_class1:
            j+=1

            cur_node=queue_class1.pop(0)
            cur_up_down={}
            res=[1]
           # adj=(sigmoid(np.sqrt(j))*np.random.normal(1))/np.sum(res)

            adj=sigmoid(np.sqrt(j/3600*24))/np.mean(res)
            res.append(adj)
            #adj=0
           # print('adj',adj)
            cur_up_down['up']=cur_node.up_node
            cur_up_down['up_prob']=cur_node.up_prob

            cur_up_down['expect_value']=adj+cur_node.elem+(cur_node.up_prob*cur_node.up_node+cur_node.down_prob*cur_node.down_node)
            #cur_up_down['expect_value'] =(cur_node.up_node+cur_node.down_node)*S0

            cur_up_down['down']=cur_node.down_node
            cur_up_down['down_prob']=cur_node.down_prob
            a.append(cur_up_down)



            cur_node.up_node =Node(cur_node.up_node,last_prob= 1  ,up_num=up_num, down_num=down_num, up_prob=up_prob,
                 down_prob=down_prob)

            cur_node.down_node=Node(cur_node.down_node,last_prob=last_prob,up_num=up_num, down_num=down_num, up_prob=up_prob,
                 down_prob=down_prob)
            cur_node.up_prob = Node(cur_node.up_prob,up_num=up_num, down_num=down_num, up_prob=up_prob,
                 down_prob=down_prob)
            cur_node.down_prob = Node(cur_node.down_prob,up_num=up_num, down_num=down_num, up_prob=up_prob,
                 down_prob=down_prob)

            queue_class1.append(cur_node.up_node)

            queue_class1.append(cur_node.down_node)
            queue_class1.append(cur_node.up_prob)
            queue_class1.append(cur_node.down_prob)
            if j==2**(self.layer+1)-1:
                break
        return a,a[2**(self.layer)-1:]


#if __name__=='__main__':

import time

a=100
S0=123.3234
def Main(start):
    aaaa=[]
    q1 = time.time()
    full_raw={}
    for w in range(start,start+1):
        full_raw[str(start)+'-'+str(start+5)]=[]
        q=Tree(layer=1)
        int=0.7753233454

        full_nodes,last_layer=q.generate(start=a,last_prob=1, up_num=1.1111,down_num=0.99999,up_prob=int,down_prob=1-int)
        expect=[last_layer[i]['expect_value'] for i in range(len(last_layer))]
       # print(expect)
        aaaa.append(np.mean(expect))
        full_raw[str(start)+'-'+str(start+5)].append(expect)
        #print(np.mean(expect))

    print('totol:',np.mean(aaaa))
    print('%dto%d time_used:' % (start, start + 5), time.time() - q1)
    return start,np.mean(aaaa),full_raw





import multiprocessing
pools=multiprocessing.Pool(processes=10)

result=[]
for v in range(0,1,1):

    result.append(pools.apply_async(Main,args=(v,)))

pools.close()
pools.join()

qqqq={}
full=[]
for no in result:

    index,every_five_mean_value,every_five_full_value=no.get()
    full.append(every_five_full_value)
    qqqq[str(index)+'-'+str(index+5)]=every_five_mean_value





#a=full_nodes[_+1]['middle']
#q.generate(start=expect[0] )
# plt.hist(expect,bins=70)
# plt.show()
#last_layer=w[2:]
#q.add(5)


