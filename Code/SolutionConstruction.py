from createSolution import createSolution
from Constructions import GRASPConstruction, greedyConstruction, RandomConstruction
from AuxFunctions import isBest

# Función que crea una solución según el método y el número de construcciones 
# indicados

def SolutionConstruction(instance, num_constructions = 100, 
                           construction_method = 'Greedy'):
    
    best_solution = createSolution(instance)
    
    if (construction_method == 'Greedy'):
        
        for i in range(num_constructions):
            
            solution = createSolution(instance)
            solution = greedyConstruction(solution)
            
            if isBest(solution, best_solution):
                
                best_solution = solution
            
            
    elif (construction_method == 'GRASP'):
        
        for i in range(num_constructions):
            
            solution = createSolution(instance)
            solution = GRASPConstruction(solution)
            
            if isBest(solution, best_solution):
                
                best_solution = solution
            
    elif (construction_method == 'Random'):
        
        for i in range(num_constructions):
            
            solution = createSolution(instance)
            solution = RandomConstruction(solution)
            
            if isBest(solution, best_solution):
                
                best_solution = solution
            
         
    return best_solution