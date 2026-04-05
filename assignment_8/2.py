import random
graph = [
    [0,10,15,20,25,30,35,40],
    [12,0,35,15,20,25,30,45],
    [25,30,0,10,40,20,15,35],
    [18,25,12,0,15,30,20,10],
    [22,18,28,20,0,15,25,30],
    [35,22,18,28,12,0,40,20],
    [30,35,22,18,28,32,0,15],
    [40,28,35,22,18,25,12,0]
]
num_cities = len(graph)
def tour_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]
    return cost



def create_chromosome():
    path = list(range(num_cities))
    random.shuffle(path)
    return path



def initial_population(size):
    return [create_chromosome() for i in range(size)]



def selection(population):
    population.sort(key=lambda x: tour_cost(x))
    return population[:2]



def one_point_crossover(p1, p2):

    point = random.randint(1, num_cities-2)

    child = p1[:point]

    for city in p2:
        if city not in child:
            child.append(city)

    return child



def two_point_crossover(p1, p2):

    p1_i = random.randint(1, num_cities-3)
    p2_i = random.randint(p1_i+1, num_cities-1)

    child = [None]*num_cities

    child[p1_i:p2_i] = p1[p1_i:p2_i]

    pointer = 0
    for city in p2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city

    return child

def mutation(path):

    i = random.randint(0, num_cities-1)
    j = random.randint(0, num_cities-1)

    path[i], path[j] = path[j], path[i]

    return path


def genetic_algorithm(pop_size, generations, crossover_type):

    population = initial_population(pop_size)

    best_solution = population[0]
    best_cost = tour_cost(best_solution)

    for g in range(generations):

        parent1, parent2 = selection(population)

        if crossover_type == "one":
            child = one_point_crossover(parent1, parent2)
        else:
            child = two_point_crossover(parent1, parent2)

        if random.random() < 0.2:
            child = mutation(child)

        population.append(child)

        population.sort(key=lambda x: tour_cost(x))
        population = population[:pop_size]

        cost = tour_cost(population[0])

        if cost < best_cost:
            best_cost = cost
            best_solution = population[0]

    best_solution.append(best_solution[0])

    print("Best Path:", best_solution)
    print("Cost:", best_cost)

    return best_solution, best_cost


print("one point crossover")
genetic_algorithm(20, 200, "one")

print("two  poinnt crossover")
genetic_algorithm(20, 200, "two")
# so here also convergence depends on the points of cross over for one point cross over we have less exploration space we have less diversity
# so we have a higher chance of getting a local optimum 
# but in case of two point cross over we have a bigger exploration space and greater diversity so have a lower chance of convegence
# that is getting stuck in local optimum