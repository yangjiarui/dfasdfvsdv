#-*-coding:utf-8-*-
'''

@author:HANDSOME_JERRY
@time:'18-6-6下午10:45'
'''

s=0
end=123
def hehe(x):
    global s
    if x==end:
        return
    else:
        s+=12**x
        x+=1
        hehe(x)
q=hehe(0)
