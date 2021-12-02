# libraries to include
from random import sample, randrange, random, shuffle
from itertools import permutations
import matplotlib.pyplot as plt

# parameters
population_size = 100
mutation_rate = .8

# answers(for checking if the fitness function works correctly, it should return 1 for all the elements in this list)
answer = [[6, 4, 2, 0, 5, 7, 1, 3], [4, 1, 5, 0, 6, 3, 7, 2], [2, 6, 1, 7, 4, 0, 3, 5], [5, 2, 0, 7, 4, 1, 3, 6],
          [3, 6, 2, 7, 1, 4, 0, 5], [5, 3, 1, 7, 4, 6, 0, 2], [1, 7, 5, 0, 2, 4, 6, 3], [3, 1, 4, 7, 5, 0, 2, 6],
          [5, 1, 6, 0, 3, 7, 4, 2], [3, 0, 4, 7, 1, 6, 2, 5], [3, 0, 4, 7, 5, 2, 6, 1], [0, 6, 3, 5, 7, 1, 4, 2],
          [5, 2, 6, 1, 7, 4, 0, 3], [4, 6, 3, 0, 2, 7, 5, 1], [5, 3, 6, 0, 7, 1, 4, 2], [1, 5, 0, 6, 3, 7, 2, 4],
          [5, 2, 0, 6, 4, 7, 1, 3], [3, 1, 6, 4, 0, 7, 5, 2], [3, 7, 4, 2, 0, 6, 1, 5], [4, 0, 3, 5, 7, 1, 6, 2],
          [4, 7, 3, 0, 6, 1, 5, 2], [0, 4, 7, 5, 2, 6, 1, 3], [2, 4, 1, 7, 5, 3, 6, 0], [3, 5, 7, 2, 0, 6, 4, 1],
          [2, 6, 1, 7, 5, 3, 0, 4], [5, 7, 1, 3, 0, 6, 4, 2], [3, 1, 7, 4, 6, 0, 2, 5], [4, 6, 0, 3, 1, 7, 5, 2],
          [2, 5, 1, 6, 0, 3, 7, 4], [5, 2, 4, 6, 0, 3, 1, 7], [3, 7, 0, 2, 5, 1, 6, 4], [2, 4, 1, 7, 0, 6, 3, 5],
          [1, 5, 7, 2, 0, 3, 6, 4], [1, 6, 2, 5, 7, 4, 0, 3], [3, 1, 7, 5, 0, 2, 4, 6], [4, 2, 7, 3, 6, 0, 5, 1],
          [7, 1, 3, 0, 6, 4, 2, 5], [5, 1, 6, 0, 2, 4, 7, 3], [4, 0, 7, 5, 2, 6, 1, 3], [5, 0, 4, 1, 7, 2, 6, 3],
          [0, 5, 7, 2, 6, 3, 1, 4], [6, 3, 1, 4, 7, 0, 2, 5], [0, 6, 4, 7, 1, 3, 5, 2], [2, 5, 7, 1, 3, 0, 6, 4],
          [5, 3, 6, 0, 2, 4, 1, 7], [6, 3, 1, 7, 5, 0, 2, 4], [6, 1, 3, 0, 7, 4, 2, 5], [2, 5, 7, 0, 3, 6, 4, 1],
          [7, 2, 0, 5, 1, 4, 6, 3], [4, 1, 3, 5, 7, 2, 0, 6], [4, 2, 0, 6, 1, 7, 5, 3], [1, 3, 5, 7, 2, 0, 6, 4],
          [4, 2, 0, 5, 7, 1, 3, 6], [2, 4, 7, 3, 0, 6, 1, 5], [1, 6, 4, 7, 0, 3, 5, 2], [7, 1, 4, 2, 0, 6, 3, 5],
          [4, 1, 7, 0, 3, 6, 2, 5], [4, 1, 3, 6, 2, 7, 5, 0], [2, 5, 7, 0, 4, 6, 1, 3], [2, 0, 6, 4, 7, 1, 3, 5],
          [1, 4, 6, 3, 0, 7, 5, 2], [2, 5, 3, 1, 7, 4, 6, 0], [4, 7, 3, 0, 2, 5, 1, 6], [3, 1, 6, 2, 5, 7, 0, 4],
          [4, 6, 1, 5, 2, 0, 7, 3], [3, 1, 6, 2, 5, 7, 4, 0], [5, 2, 4, 7, 0, 3, 1, 6], [4, 6, 1, 3, 7, 0, 2, 5],
          [6, 0, 2, 7, 5, 3, 1, 4], [4, 6, 1, 5, 2, 0, 3, 7], [6, 1, 5, 2, 0, 3, 7, 4], [3, 6, 0, 7, 4, 1, 5, 2],
          [2, 5, 1, 4, 7, 0, 6, 3], [3, 7, 0, 4, 6, 1, 5, 2], [4, 6, 0, 2, 7, 5, 3, 1], [5, 2, 0, 7, 3, 1, 6, 4],
          [3, 6, 4, 1, 5, 0, 2, 7], [1, 4, 6, 0, 2, 7, 5, 3], [2, 4, 6, 0, 3, 1, 7, 5], [4, 0, 7, 3, 1, 6, 2, 5],
          [3, 5, 0, 4, 1, 7, 2, 6], [2, 5, 3, 0, 7, 4, 6, 1], [5, 2, 6, 3, 0, 7, 1, 4], [6, 2, 7, 1, 4, 0, 5, 3],
          [2, 7, 3, 6, 0, 5, 1, 4], [3, 6, 4, 2, 0, 5, 7, 1], [5, 2, 6, 1, 3, 7, 0, 4], [6, 2, 0, 5, 7, 4, 1, 3],
          [2, 5, 1, 6, 4, 0, 7, 3], [5, 3, 0, 4, 7, 1, 6, 2], [7, 3, 0, 2, 5, 1, 6, 4], [3, 5, 7, 1, 6, 0, 2, 4]]


def fitness_evaluation(permutation, which_func):
    """
    This function calculates the sum of penalties for each configuration.
    :param permutation: the configuration
    :return: the inverse of the sum of penalties for a permutation
    """
    sum_of_penalties = 0
    # print(f"conflicts for permutation{permutation}")
    for index, queen in enumerate(permutation):
        # print(f"conflicts for queen number {queen} in index {index}:")
        for i in range(0, 8):
            distance = abs(index - i)
            # print(f"for {queen} and distance {distance} there might be conflict with {permutation[i]} if it is in positon {queen+distance} or {queen - distance}")
            if permutation[i] == queen + distance and (queen + distance) >= 0 and (
                    queen + distance) <= 7 and distance != 0:
                # print(f"{i} There was a conflict with {permutation[i]} in position {queen + i}")
                sum_of_penalties += 1
            if permutation[i] == queen - distance and (queen - distance) >= 0 and (
                    queen - distance) <= 7 and distance != 0:
                # print(f"{i}There was a conflict with {permutation[i]} in position {queen - i}")
                sum_of_penalties += 1
    if sum_of_penalties == 0:
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(permutation, which_func)
    return 1 / (sum_of_penalties + 1)


def overall_population_fitness(population):
    """

    :param population:
    :return:
    """
    sum = 0
    for permutation in population:
        sum += fitness_evaluation(permutation, "overall")
    return sum / population_size


def generate_population():
    """
    :return: the first generation,and for visualizing the results and not getting the answer in the first generation, the first generation is empty from the answers
    """
    population = []
    permutation_list = list(permutations(range(0, 8)))
    shuffle(permutation_list)
    for i in permutation_list:
        if list(i) in answer:
            permutation_list.remove(i)
    for i in range(population_size):
        population += [list(permutation_list[i])]
    return population


def recombination(parent1, parent2):
    """

    :param parent1:
    :param parent2:
    :return: cut-and-crossfill cross-over operator is implemented in this function
    """
    crossover_point = randrange(0, 7)  # not 0 and 8
    offspring1 = parent1[:crossover_point]
    offspring1 = offspring1 + [i for i in parent2[crossover_point:] if i not in offspring1]
    offspring1 = offspring1 + [i for i in parent1[crossover_point:] if i not in offspring1]
    offspring2 = parent2[:crossover_point]
    offspring2 = offspring2 + [i for i in parent1[crossover_point:] if i not in offspring2]
    offspring2 = offspring2 + [i for i in parent2[crossover_point:] if i not in offspring2]
    if len(offspring1) != 8 or len(offspring2) != 8:
        # print(offspring1)
        print("helllooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    return offspring1, offspring2


def mutation(parent):
    """

    :param parent:
    :return: a child with mutation(swapping in its genes)
    """
    random_genes = sample(range(0, 7), 2)  # index out of range nmide?
    random_genes.sort()
    first_index = random_genes[0]
    second_index = random_genes[1]
    first = parent[first_index]
    second = parent[second_index]
    parent[second_index] = first
    parent[first_index] = second
    # print(first_index,first,second_index,second)
    offspring = parent
    # print("lennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn: ", len(offspring))
    return offspring


def parent_selection(population):
    """

    :param population:
    :return: two best out of five random parents from the population is chosen
    """
    fitness_per_parent = []
    parents = sample(population, 5)
    for parent in parents:
        fitness_per_parent += [[fitness_evaluation(parent, "parent selection"), parent]]
    # print(fitness_per_parent)
    fitness_per_parent.sort()
    fitness_per_parent.reverse()
    best1, best2 = fitness_per_parent[0][1], fitness_per_parent[1][1]
    # print(best1,best2)
    return best1, best2


def survival_selection(population, offspring):
    """

    :param population:
    :param offspring:
    :return:
    """
    fitness_per_chromosome = []
    population.append(offspring)
    for chromosome in population:
        fitness_per_chromosome += [[fitness_evaluation(chromosome, "survival selection"), chromosome]]
    fitness_per_chromosome.sort()
    fitness_per_chromosome.reverse()
    fitness_per_chromosome.pop()
    new_population = [element[1] for element in fitness_per_chromosome]
    return new_population


def next_generation(current_population):
    """

    :param current_population:
    :return: applys recombination and mutation, and makes the next generation
    """
    # parent selection:
    parent1, parent2 = parent_selection(current_population)
    # recombination
    offspring1, offspring2 = recombination(parent1, parent2)
    if random() < mutation_rate:
        offspring1 = mutation(offspring1)
        offspring2 = mutation(offspring2)

    # survival selection
    inserted_first_child = survival_selection(current_population, offspring1)
    next_gen = survival_selection(inserted_first_child, offspring2)
    return next_gen


def check_solution(population):
    """

    :param population:
    :return: searches through the population and checks if the solution is found(solution hass fitness score of 1)
    """
    # print(f"overall mean fitness {overall_population_fitness(population)}")
    for chromosome in population:
        fitness_score = fitness_evaluation(chromosome, "check solution")
        # print(f"fitness score: {fitness_score: .5f} for permutaion: {chromosome} ")
        if fitness_score >= 1:  #
            print("solution found.")
            return True
    # print("solution not found in this generation.")
    return False


def genetic_algorithm():
    """

    :return: for checking the algorithm and the effect of population size
    on number of generations which leads to answer,
    this function returns the number of generations which the algorithm has to run in order to find the answer
    """
    generation_index = 0
    population = generate_population()
    while not (generation_index == 10000):
        if not (check_solution(population)):
            print(f"generation: {generation_index}")
            population = next_generation(population)
            generation_index += 1
        # if check_solution(population):
        else:
            return generation_index
    return 9999


def test_algorithm():
    """
    run the algorithm for different population sizes
    and see its effect on the algorithm
    :return:
    """
    global population_size
    x = []
    y = []
    for size in range(10, 500, 10):
        population_size = size
        x.append(size)
        mean_generations_needed = 0
        for iter in range(10):
            mean_generations_needed += genetic_algorithm()
        mean_generations_needed /= 10
        y.append(mean_generations_needed)

    plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    genetic_algorithm()
