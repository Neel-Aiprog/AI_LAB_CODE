import random
graph = [
    [0, 10, 15, 20, 25, 30, 35, 40],
    [12, 0, 35, 15, 20, 25, 30, 45],
    [25, 30, 0, 10, 40, 20, 15, 35],
    [18, 25, 12, 0, 15, 30, 20, 10],
    [22, 18, 28, 20, 0, 15, 25, 30],
    [35, 22, 18, 28, 12, 0, 40, 20],
    [30, 35, 22, 18, 28, 32, 0, 15],
    [40, 28, 35, 22, 18, 25, 12, 0]
]
num_cities = len(graph)
def get_neighbours(city, k, visited):
    distances = []
    for i in range(num_cities):
        if i != city and i not in visited:
            distances.append((graph[city][i], i))

    distances.sort(key=lambda x:x[1])  
    neighbours = [city for (i, city) in distances[0:k]]

    return neighbours



def select_best_k_neighbours(neighbours, k):
    neighbours = list(set(neighbours))
    neighbours.sort()
    return neighbours[:k]


def tour_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    return cost


def build_path(start_city, k):

    path = [start_city]
    visited = set(path)

    current_states = [start_city]

    while len(path) < num_cities:

        all_neighbours = []

        for city in current_states:
            neighbours = get_neighbours(city, k, visited)
            all_neighbours.extend(neighbours)


        if not all_neighbours:

            break

        next_states = select_best_k_neighbours(all_neighbours, k)

        next_city = next_states[0]

        path.append(next_city)
        visited.add(next_city)

        current_states = next_states

    path.append(start_city)

    return path


def travelling_salesman(graph, k, max_iterations):

    current_states = random.sample(range(num_cities), k)

    for iteration in range(max_iterations):

        all_neighbours = []

        for city in current_states:
            neighbours = get_neighbours(city, k, set())
            all_neighbours.extend(neighbours)

        next_states = select_best_k_neighbours(all_neighbours, k)

        if sorted(next_states) == sorted(current_states):
            print("Local optimum reached")
            break

        current_states = next_states

    best_start = current_states[0]
    path = build_path(best_start, k)
    cost = tour_cost(path)

    print("Complete Path:", " → ".join(map(str, path)))
    print("Total Tour Cost:", cost)

    return path, cost


(travelling_salesman(graph, 3, 100))
(travelling_salesman(graph, 5, 100))
(travelling_salesman(graph, 1, 100))
# print(travelling_salesman(graph, 10, 100))
# now in this if convergence does depend on the value of k as the higher the k is we explore more and more neighbours and have a higher chance of finding the global optimum and the lower the k is we have a lower state space to explore and hence lower chance of findin global optimum
