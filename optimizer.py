# optimizer.py

import random
import copy

class PathOptimizer:
    def __init__(self, demand_points, supply_points, routes):
        self.demand_points = demand_points
        self.supply_points = supply_points
        self.routes = routes
        self.population_size = 50
        self.num_iterations = 100

    def optimize(self):
        population = [self.create_initial_solution() for _ in range(self.population_size)]

        for _ in range(self.num_iterations):
            population = self.genetic_operations(population)
            population = self.simulated_annealing_operations(population)

        best_solution = self.select_best_solution(population)
        return best_solution

    def create_initial_solution(self):
      
        solution = []
        for route in random.sample(self.routes, len(self.routes)):
            route_with_quantity = route.copy()
            route_with_quantity['Quantity'] = random.randint(100, 1000)  
            solution.append(route_with_quantity)
        return solution

    def genetic_operations(self, population):
        selected = self.selection(population)

        crossovered = self.crossover(selected)

        mutated = self.mutation(crossovered)
        return mutated

    def simulated_annealing_operations(self, population):
        sa_population = []
        for solution in population:
            sa_solution = self.simulated_annealing(solution)
            sa_population.append(sa_solution)
        return sa_population

    def selection(self, population):
        return random.sample(population, len(population))

    def crossover(self, population):
        crossed_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i + 1] if i + 1 < len(population) else population[0]
            child1, child2 = self.single_point_crossover(parent1, parent2)
            crossed_population.extend([child1, child2])
        return crossed_population

    def single_point_crossover(self, parent1, parent2):
        point = random.randint(1, len(self.routes) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutation(self, population):
        mutated_population = []
        for solution in population:
            if random.random() < 0.1:  
                mutated_solution = self.mutate(solution)
                mutated_population.append(mutated_solution)
            else:
                mutated_population.append(solution)
        return mutated_population

    def mutate(self, solution):
        index1, index2 = random.sample(range(len(solution)), 2)
        solution[index1], solution[index2] = solution[index2], solution[index1]
        return solution

    def simulated_annealing(self, solution):
        current_solution = copy.deepcopy(solution)
        best_solution = current_solution
        T = 1.0
        T_min = 0.00001
        alpha = 0.9
        while T > T_min:
            i = 0
            while i < 100:
                new_solution = self.mutate(current_solution)
                if self.evaluate(new_solution) < self.evaluate(current_solution):
                    current_solution = new_solution
                    if self.evaluate(current_solution) < self.evaluate(best_solution):
                        best_solution = current_solution
                i += 1
            T = T * alpha
        return best_solution

    def evaluate(self, solution):
        total_time = sum(route['Estimated_Duration'] for route in solution)
        return total_time

    def select_best_solution(self, population):
        best_solution = min(population, key=self.evaluate)
        return best_solution

    def calculate_total_time_and_cost(self, solution):
        total_time = sum(route['Estimated_Duration'] for route in solution)
        total_cost = sum(route['Cost'] for route in solution)
        return total_time, total_cost
