# -*- coding: utf-8 -*-

# Módulos útiles ajenos al trabajo

import os
import random

# Módulos creados para el trabajo

from readInstances import ReadInstances
from SolutionConstruction import SolutionConstruction
from TabuSearch import TabuSearch
from SBTS import SBTS

# Comienzo del código

random.seed(123456789)

# Leemos las instancias que vamos a usar

instances = os.listdir('../instances')
instance = ReadInstances('../instances/' + instances[0])

# Construimos una solución GRASP


[solution_const, FaF, F] = SolutionConstruction(instance, num_constructions = 100, 
                            construction_method = 'GRASP', function = 'retroactive', beta_dist = 1, beta_cap = 0, 
                            beta_cost = 0, threesholdGRASP = 0.7, show_reps = True)


print('Solución GRASP')
print(sorted(solution_const['selected']))
print('OF: ', solution_const['of'], ' Cap: ', solution_const['capacity'], ' Min Cap:', 
      instance['B'], 'Cost: ', solution_const['cost'], 'Max Cost: ', instance['K'], 'Tiempo: ')


# Construimos una solución Tabu


[solution_const, FaF, F] = SolutionConstruction(instance, num_constructions = 50, 
                            construction_method = 'GRASP', function = 'retroactive', beta_dist = 1, beta_cap = 0, 
                            beta_cost = 0, threesholdGRASP = 0.7, show_reps = True)

solution_tabu = TabuSearch(solution_const, 5, 200)

print('Solución Tabu Search')
print(sorted(solution_tabu['selected']))
print('OF: ', solution_tabu['of'], ' Cap: ', solution_tabu['capacity'], ' Min Cap:', 
      instance['B'], 'Cost: ', solution_tabu['cost'], 'Max Cost: ', instance['K'], 'Tiempo: ')

# Construimos una solución SBTS

[solution_const, FaF, F] = SolutionConstruction(instance, num_constructions = 50, 
                            construction_method = 'GRASP', function = 'retroactive', beta_dist = 1, beta_cap = 0, 
                            beta_cost = 0, threesholdGRASP = 0.7, show_reps = True)

solution_sbts = SBTS(solution_const, 400)

print('Solución SBTS')
print(sorted(solution_sbts['selected']))
print('OF: ', solution_sbts['of'], ' Cap: ', solution_sbts['capacity'], ' Min Cap:', 
      instance['B'], 'Cost: ', solution_sbts['cost'], 'Max Cost: ', instance['K'], 'Tiempo: ')


