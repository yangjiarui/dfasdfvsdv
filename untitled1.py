# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:37:22 2018

@author: 834235185
"""

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

class Option(object):

    def __init__(self,s0,sigma,r,t,n,k,type=''):
        self.s0=s0
        self.sigma=sigma
        self.r=r
        self.t=t
        self.n=n
        self.k=k
        self.type=type


    def Eu_price(self):
        time=float(self.t)/self.n
        u=math.exp(self.sigma*time**0.5)
        d=math.exp(-self.sigma*time**0.5)
        p=(math.exp(self.r*time)-d)/(u-d)
        payment=0
        for i in range(self.n+1):
            if self.type=='Call':
                pay=max(((self.s0*u**(self.n-2*i))-self.k),0)
            elif self.type=='Put':
                pay=max(self.k-((self.s0*u**(self.n-2*i))),0)
            ppay=pay*nCr(self.n,i)*((1-p)**i)*(p**(self.n-i))
            payment+=ppay
        payment=payment/math.exp(self.r*self.t)
        return payment

#××××××××××××××××××××××××××××××××××××××××××××××#

newoption = Option(100.0,0.2,0.05,1.0,100,100.0,type='Put')

print (newoption.Eu_price())
#××××××××××××××××××××××××××××××××××××××××××××××#

#美式期权作为可以提前practice的期权，就复杂的多。

#可以先定义一个List，然后向前递归，取节点价值（practice）和发展价值的较大值。起点的价值就是定价。

 

import math

class Option(object):

    def __init__(self,s0,sigma,r,t,n,k,type=''):
        self.s0=s0
        self.sigma=sigma
        self.r=r
        self.t=t
        self.n=n
        self.k=k
        self.type=type


    def Am_price(self):
        time=float(self.t)/self.n
        u=math.exp(self.sigma*time**0.5)
        d=math.exp(-self.sigma*time**0.5)
        p=(math.exp(self.r*time)-d)/(u-d)
        pay=[]
        for i in range(self.n+1):
            if self.type=='Call':
                pay.append(max(((self.s0*u**(self.n-2*i))-self.k),0))
            elif self.type=='Put':
                pay.append(max((self.k-(self.s0*u**(self.n-2*i))),0))

        for j in range(self.n-1,-1,-1):
            ppay=[]
            qpay=[]
            for m in range(j+1):
                if self.type=='Call':
                    qpay.append((max(((self.s0*u**(j-2*m))-self.k),0)))
                elif self.type=='Put':
                    qpay.append((max((self.k-(self.s0*u**(j-2*m))),0)))
                ppay.append((pay[m]*p+pay[m+1]*(1-p))*math.exp(-self.r*time))

                pay[m]=max(qpay[m],ppay[m])
        return pay[0]

#在定价的基础上，Greek就很容易得到了，只需要取一个极小的变化值，然后得到微分即可。

def delta(self):
        ds=0.1
        new=Option(self.s0,self.sigma,self.r,self.t,self.n,self.k,self.type)
        new1=Option(self.s0+ds,self.sigma,self.r,self.t,self.n,self.k,self.type)
        return (new1.Am_price()-new.Am_price())/ds
def gamma(self):
    ds=0.1
    new=Option(self.s0,self.sigma,self.r,self.t,self.n,self.k,self.type)
    new1=Option(self.s0+ds,self.sigma,self.r,self.t,self.n,self.k,self.type)
    return (new1.delta()-new.delta())/ds

def vega(self):
    dsigma=0.0001
    new=Option(self.s0,self.sigma,self.r,self.t,self.n,self.k,self.type)
    new1=Option(self.s0,self.sigma+dsigma,sel)