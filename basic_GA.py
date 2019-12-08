import numpy as np
import matplotlib.pyplot as plt
import statistics 

class GA(object):
    def __init__(self, population_size, chromosome_size, N_gerneration, crossover_rate=0.8, mutation_rate=0.003,  X_bound=[0,5]):

        self.population_size = population_size            # DNA length
        self.chromosome_size = chromosome_size           # population size
        # mating probability (DNA crossover)
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate     # mutation probability
        self.N_gerneration = N_gerneration
        self.X_bound = X_bound          # x upper and lower bounds
        self.main_loop()
        

    def pop(self):return np.random.randint(2, size=(self.population_size, self.chromosome_size))

    def F(self, x):
        # to find the maximum of this function
        return np.sin(10*x)*x + np.cos(2*x)*x

    def select(self, population, fitness):
        # TODO: can test the result will be different or not if using replace=false
        # np.random.choice(a, size=None, replace=True, p=None)
        # where replacement means that whether can re-sample or not
        idx = np.random.choice(np.arange(self.population_size), size=self.population_size, replace=True,
                           p=fitness/fitness.sum())
        print("The fitted idx is :", idx)        
        return population[idx]

    def crossover(self, original_parent, parent_to_crossover):
        if np.random.rand() < self.crossover_rate:
            i_ = np.random.randint(0, self.population_size, size=1)
            crossover_points = np.random.randint(0, 2, size=self.chromosome_size).astype(np.bool)
            original_parent[crossover_points] = parent_to_crossover[i_, crossover_points]
        return original_parent
            

    # find non-zero fitness for selection
    def get_fitness(self, pred): return pred + 1e-3 - np.min(pred)

    def mutate(self, child):
        for point in range(self.chromosome_size):
            if np.random.rand() < self.mutation_rate:
                child[point] = 1 if child[point] == 0 else 0
        return child

    # convert binary DNA to decimal and normalize it to a range(0, 5)
    def translate_bi_to_dex(self, population):
        decimal = population.dot((2 ** np.arange(self.chromosome_size)[::-1])) / float(2**self.chromosome_size-1) * self.X_bound[1]
        return decimal
    
    def main_loop(self):
        population = self.pop()
        for t in range(self.N_gerneration):
            F_value = self.F(self.translate_bi_to_dex(population))
            fitness = self.get_fitness(F_value)
            print(statistics.mean(fitness))
            print("Most fitted DNA is in pop: %d" %np.argmax(fitness),)
            print("Most fitted DNA:", population[np.argmax(fitness)][:],)
            population = self.select(population, fitness)
            population_copy = population.copy()
            for parent in population:
                child = self.crossover(parent, population_copy)
                child = self.mutate(child)
                parent[:] = child
                # print('child is : ', child)
                # print('parent is : ', parent)
                
            print('-------------epoch % i----------------'%t)


if __name__ == "__main__":

    test = GA(10,15,10)
    
    # a.crossover()
    print('run out of this py file')

    
