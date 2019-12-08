import numpy as np
import time as ti
import random as ra

METHOD = [
    dict(name='mini'),  # minimal
    dict(name='maxi')   # maximum
][1]  # choose the method for optimization
      # TODO: add this

class OOP_SSO(object):
    def __init__(self, N_sol, N_var, N_iter, Cg, Cp, Cw, VarMax, VarMin, CPUTime):
        self.N_sol = N_sol
        self.N_var = N_var
        self.N_iter = N_iter
        self.Cg = Cg
        self.Cp = Cp
        self.Cw = Cw
        self.VarMax = VarMax
        self.VarMin = VarMin
        self.CPUTime = CPUTime

        self.empty_sol_content = {
            'sol': None, 'solFitness': None, 'pbestSol': None, 'pbestFitness': None}

    # fitness func
    def fitness(self, x):
        return sum(x**2)

    def _init(self):
        # _iter_solContent
        gbest = 0
        solContent = []
        startTime = ti.time()
        self.startTime = startTime

        for i in range(self.N_sol):
            solContent.append(self.empty_sol_content.copy())
            solContent[i]['sol'] = np.random.uniform(
                self.VarMin, self.VarMax, self.N_var)
            solContent[i]['pbestSol'] = solContent[i]['sol']
            solContent[i]['solFitness'] = self.fitness(
                solContent[i]['sol'])
            solContent[i]['pbestFitness'] = solContent[i]['solFitness']
            if solContent[i]['solFitness'] < solContent[gbest]['solFitness']:
                gbest = i

        self.gbest = gbest
        self.solContent = solContent
        return self.solContent

    # main loop
    def count_time(self):

        # use countTime record run time
        currentTime = ti.time()
        self.countTime = currentTime-self.startTime

        return self.countTime

    def dice(self):
        dice_solContent = self._iter_solContent
        for i in range(self.N_sol):
            for k in range(self.N_var):
                r = ra.random()
                if r < self.Cw:
                    pass
                elif r < self.Cp:
                    dice_solContent[i]['sol'][k] = dice_solContent[i]['pbestSol'][k]
                elif r < self.Cg:
                    dice_solContent[i]['sol'][k] = dice_solContent[self.gbest]['pbestSol'][k]
                else:
                    dice_solContent[i]['sol'][k] = ra.uniform(
                        self.VarMin, self.VarMax)
            dice_solContent[i]['solFitness'] = self.fitness(
                dice_solContent[i]['sol'])

            # update pbst、self.gbest
            if dice_solContent[i]['solFitness'] < dice_solContent[i]['pbestFitness']:
                dice_solContent[i]['pbestSol'] = dice_solContent[i]['sol'].copy(
                )
                dice_solContent[i]['pbestFitness'] = dice_solContent[i]['solFitness']
                if dice_solContent[i]['pbestFitness'] < dice_solContent[self.gbest]['pbestFitness']:
                    self.gbest = i
        self._iter_solContent = dice_solContent

    def main_process(self):

        # get init and time
        self._iter_solContent = self._init()
        countTime = self.count_time()

        # main_process
        for t in range(self.N_iter):
            if countTime < self.CPUTime:
                dice_process = self.dice()
                # print('In iteration', t, ',The best cost is:',_iter_solContent[self.gbest]['pbestFitness'])
                # print('Global best #:', self.gbest)
                # record the run time during iteration
                countTime = self.count_time()
            else:
                print('\nMeet the CPUTime!!\n')
                break

        # show result
        print('the best cost is:',
              self._iter_solContent[self.gbest]['pbestFitness'])
        # print('Global best:', _iter_solContent[self.gbest]['pbestSol'])
        print(self.gbest)
        # print('Elapsed time is:', format(countTime, '.2f'))

        return self._iter_solContent[self.gbest]['pbestFitness']


if __name__ == '__main__':
    SSO = OOP_SSO(N_sol=10, N_iter=10, N_var=3, Cg=0.8, Cp=0.5,
                  Cw=0.2, VarMax=5, VarMin=-5, CPUTime=100)

    SSO_Buffer = []
    for i in range(1):
        SSO_Buffer.append(SSO.main_process().copy())
