from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
from django.http import HttpResponse

import random
import math
import numpy as np
message=''

def rao2Algo(Max_iter,SearchAgents_no,lower_val,upper_val):
    maxfes = 500000  # Maximum functions evaluation
    lenvar=4#changelenvar
    # SearchAgents_no = 10  # Population size
    # Max_iter = math.floor(maxfes / SearchAgents_no)  # Maximum number of iterations
    # Max_iter = 100
    lb = lower_val * np.ones(lenvar)  # lower bound
    ub = upper_val * np.ones(lenvar)  # upper bound
    var1=[]
    global message
    
    
    def fitness(x):
        return (x[0]**2)-(x[1]**3)+(x[2]**2)+(x[3]**2)#changeequation


    Positions = np.zeros((SearchAgents_no, lenvar)) # search agent position
    best_pos = np.zeros(lenvar) # search agent's best position
    worst_pos = np.zeros(lenvar) # search agent's worst position

    finval = np.zeros(Max_iter) # best score of each iteration
    f1 = np.zeros(SearchAgents_no) # function value of current population
    f2 = np.zeros(SearchAgents_no) # function value of updated population
    for i in range(lenvar):
        Positions[:, i] = np.random.uniform(0,1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]
    for k in range(0,Max_iter):
        best_score = float("inf")
        worst_score = float("-inf")
        for i in range(0,SearchAgents_no):

            # Return back the search agents that go beyond the boundaries of the search space
            for j in range(lenvar):
                Positions[i,j]=np.clip(Positions[i,j], lb[j], ub[j])

            f1[i]= fitness(Positions[i,:])
            if f1[i] < best_score :
                best_score=f1[i].copy(); # Update best
                best_pos=Positions[i,:].copy()
                var1.clear()
                for val in range(0,lenvar):
                    var1.append(Positions[i,:][val])
            if f1[i] > worst_score :
                worst_score=f1[i].copy(); # Update worst
                worst_pos=Positions[i,:].copy()
        # Update the Position of search agents including omegas
        finval[k] = best_score
        Positioncopy = Positions.copy()
        r = np.random.randint(SearchAgents_no, size=1)
        message+="The best solution is: "+str(best_score) + " in iteration number: "+str(k+1)+"\n"
        
        for i in range(0,SearchAgents_no):
            if (f1[i] < f1[r]):
                for j in range (0,lenvar):
                    r1=random.random() # r1 is a random number in [0,1]
                    r2=random.random() # r1 is a random number in [0,1]
                    Positions[i,j]= Positions[i,j] + r1*(best_pos[j]-worst_pos[j]) + r2*(np.abs(Positions[i,j])-np.abs(Positions[r,j]))#change in position
                    Positions[i,j]=np.clip(Positions[i,j], lb[j], ub[j])
            else :
                for j in range (0,lenvar):
                    r1=random.random() # r1 is a random number in [0,1]
                    r2=random.random() # r1 is a random number in [0,1]
                    Positions[i,j]= Positions[i,j] + r1*(best_pos[j]-worst_pos[j]) + r2*(np.abs(Positions[r,j])-np.abs(Positions[i,j]))#change in position
                    Positions[i,j]=np.clip(Positions[i,j], lb[j], ub[j])
                f2[i] = fitness(Positions[i,:])
            for i in range(0,SearchAgents_no):
                if (f1[i] < f2[i]):
                    Positions[i,:] = Positioncopy[i,:]
    best_score = np.amin(finval)
    message+="The best solution is: "+str(best_score)+" pos "+str(best_pos[0])+" "+str(worst_pos[-1])
    return best_score,var1,Positions

def home(request):
    return render(request,'codeapp/home.html')
def code(request):
    if request.method=="POST":
        query=request.POST['array']
        returnstring='jaya algo'
        return HttpResponse('Sorted Array : '+returnstring)

    return HttpResponse('Please give input')


def check(request):
    popsize=int(request.GET['popsize'])
    lb=int(request.GET['lb'])
    ub=int(request.GET['ub'])
    gen=int(request.GET['gen'])
    x,y,z=rao2Algo(gen,popsize,lb,ub)
    return JsonResponse({'best':str(x),'algo-coordi':str(y),'text':'Rao2 Container','Lines':z.tolist()})
