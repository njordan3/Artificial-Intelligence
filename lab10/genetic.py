import numpy as np

np.set_printoptions(threshold=10)

def fitness(ind, axis):
    # Sum 1's in individual
    return np.sum(ind, axis)

def crossover(i1, i2):
    # Concat both halves of 2 individuals
    new1 = np.concatenate((i1[0:10], i2[10:20]))
    #mutate new1
    if np.random.random() < 0.1:
        x = np.random.randint(20)
        new1[x] = not new1[x]
    new2 = np.concatenate((i2[0:10], i1[10:20]))
    #mutate new2
    if np.random.random() < 0.1:
        x = np.random.randint(20)
        new2[x] = not new2[x]
    return [new1, new2]

def tournament(pop, size):
    choices = []
    #fill choices with a number of random indexes in pop
    #make sure that no two indexes are the same
    for i in range(size):
        x = np.random.randint(len(pop))
        while x in choices:
            x = np.random.randint(len(pop))
        choices.append(x)
    #find the index of the best individual from choices
    best = choices[0]
    for i in choices:
        if fitness(pop[best], 0) < fitness(pop[i], 0):
            best = i
    return best

def elitism(pop):
    #return the index of the best in pop
    fit = fitness(pop, 1)
    best = 0
    for i in range(len(fit)):
        if fit[i] > fit[best]:
            best = i
    return best

def empty2DArray(arr):
    for i in range(len(arr)):
        arr = np.delete(arr, 0, 0)
    return arr

# M = Genome length
M = 20 # rows
# N = Population amount
N = 10 # columns
# Create an N by M 2D array full random numbers
# Threshold it to produce random true/false values
population = np.random.rand(N,M) > 0.5
print("initial population: {}".format(fitness(population, 1)))
# initialize empty 2D numpy array of shape (0, 20)
new = np.empty((N,M))
new = empty2DArray(new)

for i in range(10):
    # stop if fitness goal is reached
    if 20 in fitness(population, 1):
        print("individual found with all 1's!")
        break
    # iterate over each individual in the population
    pop_length = len(population)
    for ind in range(pop_length):
        # chance to crossover
        if np.random.random() < 0.5:
            # run tournament selection to get best of a subset
            selection = tournament(population, 3)
            # run crossover with winner of tournament
            temp = crossover(population[ind], population[selection])
            # add new individuals to a new population
            new = np.append(new, [temp[0], temp[1]], 0)
            # choose the best of the current population
            best = elitism(population)
            # add the best of the current population to the new population
            new = np.append(new, [population[best]], 0)
        #print("iteration {}-{}: new = {}".format(i+1, ind+1, fitness(new, 1)))
    # replace current population with new once all individuals have had a chance to crossover
    population = new
    # empty new population
    new = empty2DArray(new)
    print("iteration {}: {}".format(i+1, fitness(population, 1)))
