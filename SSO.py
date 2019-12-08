import numpy as np
import time as ti
import statistics
import random as ra


class SSO(object):
    def __init__(self, N_sol, N_var, N_generations, Cg=0.8, Cp=0.5, Cw=0.2, VarMax=5, VarMin=-5, CPUTime=100):
        self.N_sol = N_sol
        self.N_var = N_var
        self.N_generations = N_generations
        self.Cg = Cg
        self.Cp = Cp
        self.Cw = Cw
        self.VarMax = VarMax
        self.VarMin = VarMin
        self.CPUTime = CPUTime
        self.main_process(self.N_generations)
        
    def fitness(self, x): return sum(x**2)
        
    def main_process(self, N_generations):
        population = self._init_solContnet()
        countTime = self.count_time()
        for t in range(N_generations):
            if countTime < self.CPUTime:
                population = self.dice(population)
                countTime = self.count_time()
            else:
                print('\nMeet the CPUTime!!\n')
                break
        self.__str__(population)
            

    def dice(self, dice_object):
        for i in range(dice_object[:].__len__()):
            for j in range(self.N_var):
                r = ra.random()
                if r < self.Cw:
                    pass
                elif r < self.Cp:
                    dice_object[i]['sol'][j] = dice_object[i]['pbestSol'][j]
                elif r < self.Cg:
                    dice_object[i]['sol'][j] = dice_object[self.gbest]['pbestSol'][j]
                else:
                    dice_object[i]['sol'][j] = np.random.uniform(self.VarMin, self.VarMax)
            dice_object[i]['solFitness'] = self.fitness(
                dice_object[i]['sol'])    
            
            # update pbst、self.gbest
            if dice_object[i]['solFitness'] < dice_object[i]['pbestFitness']:
                dice_object[i]['pbestSol'] = dice_object[i]['sol'].copy(
                )
                dice_object[i]['pbestFitness'] = dice_object[i]['solFitness']
                if dice_object[i]['pbestFitness'] < dice_object[self.gbest]['pbestFitness']:
                    self.gbest = i
        return dice_object

    def _init_solContnet(self):
        self.startTime = ti.time()
        gbest = 0
        population=[]
        for i in range(self.N_sol):
            population.append({'sol': None, 'solFitness': None, 'pbestSol': None, 'pbestFitness': None})
            population[i]['sol'] = np.random.uniform(
                self.VarMin, self.VarMax, self.N_var)
            population[i]['pbestSol'] = population[i]['sol']
            population[i]['solFitness'] = self.fitness(
                population[i]['sol'])
            population[i]['pbestFitness'] = population[i]['solFitness']
            if population[i]['solFitness'] < population[gbest]['solFitness']:
                gbest = i

        self.gbest = gbest
        return population

    def count_time(self):
        # use countTime record run time
        currentTime = ti.time()
        return (lambda countTime: countTime)(currentTime - self.startTime)

    def __str__(self, population):
        return print('the best cost is:',
              population[self.gbest]['pbestFitness'],
              'the gbest: %i'% self.gbest)

if __name__ == "__main__":
    a = SSO(N_sol=10, N_generations=10, N_var=10, Cg=0.8, Cp=0.5,
                  Cw=0.2, VarMax=5, VarMin=-5 , CPUTime=10)


    print('run out of SSO')
