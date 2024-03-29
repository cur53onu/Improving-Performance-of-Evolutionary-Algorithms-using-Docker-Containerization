import math
import numpy as np
import random
import pandas as pd

#for reference https://medium.com/@dhiraj.p.rai/jaya-optimization-algorithm-16da8708691b
def myobj(p1):
    F=[]
    for i in range (len(p1)):
        x = p1.loc[i]
#         print(x.size)
        f=(x[0]**2)-(x[1]**3)+(x[2]**2)+(x[3]**2)
        F.append(f)
    return F


pop_size = 20
Gen = 60
lb=[-20,-20,-20,-20]
ub=[20,20,20,20]

#code needs to change when variables are changed
def initialpopulation(mini,maxi,pop_size,dim):
    pop=[]        
    for i in range(pop_size):
        p=[]        
#         for a,b in zip(mini,maxi):
#             p.append(a + (b-a) * random.random())
#             p.append(a + (b-a) * random.random())
        for i in range(dim):
            p.append(random.uniform(mini[0],maxi[0]))
#         print(p)
        pop.append(p)    
    ini_pop=pd.DataFrame(pop)        
    return ini_pop


def updatepopulation(p1,dim):      
    best_x=np.array(p1.loc[p1['f'].idxmin][0:dim])    
    worst_x=np.array(p1.loc[p1['f'].idxmax][0:dim])
    new_x=[]
    for i in range(len(p1)):
        old_x=np.array(p1.loc[i][0:dim])           
        r1=np.random.random(dim)
        r2=np.random.random(dim)
        new_x.append(old_x+r1*(best_x-abs(old_x))-r2*(worst_x-abs(old_x))) 
#         print("dim",dim)
#         print("loop",old_x+r1*(best_x-abs(old_x))-r2*(worst_x-abs(old_x)))
    new_p1=pd.DataFrame(new_x)    
    return new_p1

def greedyselector(p1,new_p1):    
    for i in range(len(p1)):        
        if p1.loc[i]['f']>new_p1.loc[i]['f']:                 
            p1.loc[i]=new_p1.loc[i]    
    return p1

def trimr(new_p1,lb,ub):    
    col=new_p1.columns.values    
    for i in range(len(new_p1)):        
        for j in range(len(col)):            
            if new_p1.loc[i][j]>ub[j]:                
                  new_p1.loc[i][j]=ub[j]            
            elif new_p1.loc[i][j]<lb[j]:                          
                  new_p1.loc[i][j]=lb[j]
#     print(len(new_p1))
    return new_p1

def jaya(*argv):
    pop_size, Gen, mini, maxi= argv
    lb=np.array(mini)
    ub=np.array(maxi)
    dim=len(lb)
    p1=initialpopulation(lb,ub,pop_size,dim)
#     print("p1 is ")
#     print(p1)
    p1['f']=myobj(p1)
    
    
    gen=0
    best=[]
    while (gen<Gen):
        new_p1=updatepopulation(p1,dim)
#         print("p1",p1[2])
#         print("new",new_p1[2])
        new_p1=trimr(new_p1,lb,ub)
        new_p1['f']=myobj(new_p1)
#         print("p1",len(p1))
#         print("newp1", len(new_p1))
       
        p1=greedyselector(p1,new_p1)
        gen=gen+1
    #     print(gen)
        best=p1['f'].min()
        xbest=p1.loc[p1['f'].idxmin()][0:dim].tolist()
#     print('Best={}'.format(best))
#     print('xbest={}'.format(xbest))
    return best,xbest


def main():
    best,xbest = jaya(pop_size, Gen, lb, ub)
    print('The objective function value = {}'.format(best))
    print('The optimum values of variables = {}'.format(xbest))

main()
