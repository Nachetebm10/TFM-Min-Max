import numpy as np
from evaluateSolution import evaluation, removeNode, addNode

def improveLS(solution):
    
    solutionShift = True
    while (solutionShift == True):
        
        solutionShift = False
        
        best_min_dist = 0
        
        for i in solution['selected']:
            
            # Probamos a eliminar el nodo i
            
            node_out = i
            
            # Calculamos su mínima distancia
            
            min_dist_node_out = calculateMinDist(node_out, solution)
            
            # Creamos los candidatos posibles 
            
            nodes_out_solution = [j for j in np.arange(1, solution['instance']['n']+1) if j not in solution['selected']]
        
            candidates = []
            
            for node in nodes_out_solution:
                
                new_cost = solution['cost'] - solution['instance']['k'][node_out-1] + solution['instance']['k'][node-1]
                new_capacity = solution['capacity'] - solution['instance']['b'][node_out-1] + solution['instance']['b'][node-1]
                
                if (new_cost <= solution['instance']['K'] and new_capacity >= solution['instance']['B']):
                    
                    candidates.append(node)
                
                
            # Comprobamos sí hay algún nodo que mejore la función objetivo

            solution = removeNode(node_out, solution)            
            node_in = node_out
            
            if (len(candidates) >= 1):
                
                for candidate in candidates:
                    
                    min_dist_candidate = calculateMinDist(candidate, solution)
                    
                    if (min_dist_candidate > min_dist_node_out and min_dist_candidate > best_min_dist):
                        
                        node_in = candidate
                        
                        best_min_dist = min_dist_candidate
                        
                        # Actualizamos la condición de parada
                        
                        solutionShift = True
                
            # Añadimos a la solución el nodo
            
            solution = addNode(node_in, solution)
             
    
    return solution
        


def calculateMinDist(node, solution):
    
    # Calculamos la mínima distancia del nodo con la solución
    
    distancias = [solution['instance']['m'][node-1][j-1] for j in solution['selected'] if j != node]

    min_dist = min(distancias)

    return min_dist


    

###############################################

# Si quisieramos cambiar aquel nodo que siempre tiene la menor mínima distancia

       # # Calculamos que nodo vamos a eliminar de la solución
       
       # # Calculamos las mínimas distancias de cada nodo
       
       # min_distancias = []
       
       # for i in solution['selected']:

       #     distancias = [solution['instance']['m'][i-1][j-1] for j in solution['selected'] if j != i]
            
       #     min_distancias.append(min(distancias))
           
       # candidates_out = [solution['selected'][j] for j in range(len(solution['selected'])) if solution['of'] == min_distancias[j]]
           
       # # Eliminamos aquel nodo cuya capacidad sea menor
       
       # capacidad_candidate = [solution['instance']['b'][j-1] for j in candidates_out]
       
       # min_cap = min(capacidad_candidate)
       
       # node_out = [candidates_out[j] for j in range(len(candidates_out)) if min_cap == capacidad_candidate[j]]
       
       # more_shifts = False
       
###############################################    

