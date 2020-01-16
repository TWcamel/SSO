import numpy as np
import time as ti
import random as ra
# fitness function


def fitness(x):
    return sum(x**2)


# problem description and setting parameter(can them modify in there)
problem = {'fitfun': fitness, 'Nsol': 20,
           'Niter': 10, 'Nvar': 5000,
           'cw': 0.2, 'cp': 0.5, 'cg': 0.8,
           'VarMax': 5.12, 'VarMin': -5.12,
           'CPUTime': 20}

# get problem info and parameter into variable
fitfun = problem['fitfun']
Nsol = problem['Nsol']
Niter = problem['Niter']
Nvar = problem['Nvar']
cw = problem['cw']
cp = problem['cp']
cg = problem['cg']
VarMax = problem['VarMax']
VarMin = problem['VarMin']
CPUTime = problem['CPUTime']


empty_sol_content = {'sol': None, 'solFitness': None,
                     'pbestSol': None, 'pbestFitness': None}

# loop
startTime = ti.time()
gbest = 0
solContent = []
# initialize
for i in range(0, Nsol):
    solContent.append(empty_sol_content.copy())
    solContent[i]['sol'] = np.random.uniform(VarMin, VarMax, Nvar)
    solContent[i]['pbestSol'] = solContent[i]['sol']
    solContent[i]['solFitness'] = fitfun(solContent[i]['sol'])
    solContent[i]['pbestFitness'] = solContent[i]['solFitness']
    if solContent[i]['solFitness'] < solContent[gbest]['solFitness']:
        gbest = i
# use conTime record run time
curTime = ti.time()
conTime = curTime-startTime
# iteration

for t in range(0, Niter):
    if conTime < CPUTime:
        for i in range(0, Nsol):
            for k in range(0, Nvar):
                r = ra.random()
                if r < cw:
                    pass
                elif r < cp:
                    solContent[i]['sol'][k] = solContent[i]['pbestSol'][k]
                elif r < cg:
                    solContent[i]['sol'][k] = solContent[gbest]['pbestSol'][k]
                else:
                    solContent[i]['sol'][k] = ra.uniform(VarMin, VarMax)
            solContent[i]['solFitness'] = fitfun(solContent[i]['sol'])
            # update pbst、gbest
            if solContent[i]['solFitness'] < solContent[i]['pbestFitness']:
                solContent[i]['pbestSol'] = solContent[i]['sol'].copy()
                solContent[i]['pbestFitness'] = solContent[i]['solFitness']
                if solContent[i]['pbestFitness'] < solContent[gbest]['pbestFitness']:
                    gbest = i
        # print('In iteration', t, ',the best cost is:',
            #   solContent[gbest]['pbestFitness'])
        # record the run time during iteration
        curTime = ti.time()
        conTime = curTime-startTime
    else:
        print('\nMeet the CPUTime!!\n')
        break
# show result
print('the best cost is:', solContent[gbest]['pbestFitness'])
# print('Global best:', solContent[gbest]['pbestSol'])
print('Elapsed time is:', format(conTime, '.2f'))
