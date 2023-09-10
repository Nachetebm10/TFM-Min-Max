import numpy as np
from evaluateSolution import removeNode, addNode
from AuxFunctions import improvementCL

def improveLS(solution):
    
    solutionShift = True
    
    while (solutionShift == True):
        
        solutionShift = False
        
        best_min_dist = 0
        
        for i in solution['selected']:
            
            # Probamos a eliminar el nodo i
            
            node_out = i
            
            # Calculamos su mínima distancia
            
            min_dist_node_out = solution['dist_to_S'][node_out-1,0]
            
            # Creamos los candidatos posibles 
            
            # nodes_out_solution = [j for j in np.arange(1, solution['instance']['n']+1) if j not in solution['selected']]
        
            # candidates = []
            
            # for node in nodes_out_solution:
                
            #     new_cost = solution['cost'] - solution['instance']['k'][node_out-1] + solution['instance']['k'][node-1]
            #     new_capacity = solution['capacity'] - solution['instance']['b'][node_out-1] + solution['instance']['b'][node-1]
                
            #     if (new_cost <= solution['instance']['K'] and new_capacity >= solution['instance']['B']):
                    
            #         candidates.append(node)
                
                
            solution = removeNode(node_out, solution)
            
            CL = improvementCL(solution)
            
            # Comprobamos sí hay algún nodo que mejore la función objetivo

            # solution = removeNode(node_out, solution) 
            
            node_in = node_out
            
            if (len(CL) > 0):
                
                for candidate in CL:
                    
                    if(candidate != node_out):
                        
                        min_dist_candidate = solution['dist_to_S'][candidate-1,0]
                        
                        if (min_dist_candidate > min_dist_node_out and min_dist_candidate > best_min_dist):
                            
                            node_in = candidate
                            
                            best_min_dist = min_dist_candidate
                            
                            # Actualizamos la condición de parada
                            
                            solutionShift = True
                
            # Añadimos a la solución el nodo
            
            solution = addNode(node_in, solution)
    
    return solution
        

