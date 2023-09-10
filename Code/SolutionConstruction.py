import copy
import time

from createSolution import createSolution
from Constructions import GRASPConstruction, greedyConstruction, RandomConstruction
from AuxFunctions import isBest
from LocalSearchGrasp import improveLS

# Función que crea una solución según el método y el número de construcciones 
# indicados



def SolutionConstruction(instance, num_constructions = 100, 
                           construction_method = 'Greedy', function = 'dist', beta_dist = 1/3, beta_cap = 1/3, 
                           beta_cost = 1/3, beta_dist_retro = 1, beta_ratio = 0, threesholdGRASP = 0.3, show_reps = True):
    
    feasible_at_first = 0
    feasible_before_moves = 0
    
    best_solution = createSolution(instance)
    
    time_create = time.time()
    
    if (construction_method == 'Greedy'):
        
        for i in range(num_constructions):
            
            if(show_reps):
                print('Repetición:', i)
        
            solution = createSolution(instance)
            solution, feasible_at_first, feasible_before_moves = greedyConstruction(solution, feasible_at_first, feasible_before_moves, function = function, beta_dist = beta_dist, beta_cap = beta_cap, 
                                               beta_cost = beta_cost, beta_dist_retro = beta_dist_retro, 
                                               beta_ratio = beta_ratio)
    
    
            if isBest(solution, best_solution):

                
                best_solution = copy.deepcopy(solution)
                time_best = time.time()
                best_solution['time_to_best'] = time_best - time_create
            
    elif (construction_method == 'GRASP'):
        
        for i in range(num_constructions):
            
            if(show_reps):
                print('Repetición:', i)
            
            solution = createSolution(instance)
            
            solution, feasible_at_first, feasible_before_moves = GRASPConstruction(solution, feasible_at_first, 
                    feasible_before_moves, function = function, beta_dist = beta_dist, beta_cap = beta_cap, 
                    beta_cost = beta_cost, threeshold = threesholdGRASP)
            
            # print('Solución inicial')
            # print(sorted(solution['selected']))
            # print('OF: ', solution['of'], ' Cap: ', solution['capacity'], ' Min Cap:', 
            #       instance['B'], 'Cost: ', solution['cost'], 'Max Cost: ', instance['K'])
            
            solution = improveLS(solution)
    
            if isBest(solution, best_solution):
                
                best_solution = copy.deepcopy(solution)
                time_best = time.time()
                best_solution['time_to_best'] = time_best - time_create
            
    elif (construction_method == 'Random'):
        
        for i in range(num_constructions):
            
            if(show_reps):
                print('Repetición:', i)
                
            solution = createSolution(instance)
            solution, feasible_at_first, feasible_before_moves = RandomConstruction(solution, 
                                                                                feasible_at_first, feasible_before_moves)
            
            
            if isBest(solution, best_solution):
                
                best_solution = copy.deepcopy(solution)
                time_best = time.time()
                best_solution['time_to_best'] = time_best - time_create
               
                
    return best_solution, feasible_at_first, feasible_before_moves