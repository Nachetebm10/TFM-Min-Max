import numpy as np

# Función que construye la CL para la solución actual

def constructionCL(solution):
    
    # Definimos la CL
    
    CL = []
    
    # Construimos la CL para los nodos que hay en la solucion
    
    for i in np.arange(1, solution['instance']['n']+1):
        
        if (i not in solution['selected']):
            
            coste_actualizado = solution['cost'] + solution['instance']['k'][i-1]
            
            if (coste_actualizado <= solution['instance']['K']):
                
                CL.append(i)
                
    return CL


# Función que indica si la solución es factible

def isFeasible(solution):
    
    if (len(solution['selected']) == 0):
        
        return False
    
    elif ((solution['cost'] > solution['instance']['K']) or (solution['capacity'] < solution['instance']['B'])):
        
        return False
    
    else:
        return True
    
    
# Función que devuelve si una solución es mejor que la mejor solución actual
        
def isBest(solution, best_solution):
    
    
    if (best_solution['of'] < solution['of']):
        
        return True
    
    else:
        
        return False
         


def NodeMinDist(solution):
    
    nodes_min = []
    nodes_in_solution = [i-1 for i in solution['selected']]
    
    for node in nodes_in_solution:
        
        if(min(solution['dist_to_S'][nodes_in_solution,0]) == solution['dist_to_S'][node,0]):
            
            nodes_min.append(node+1)
            
    # nodes_min = []
        
    # for i in solution['selected']:
        
    #     for j in solution['selected']:
            
            
    #         if (j != i and solution['instance']['m'][i-1][j-1] == solution['of']):
                
    #             nodes_min.append(i)
                    
    return nodes_min

        
    
def improvementCL(solution):
    
    # Definimos la CL
    
    CL = []
    
    # Construimos la CL para los nodos que hay en la solucion
    
    for i in np.arange(1, solution['instance']['n']+1):
        
        if (i not in solution['selected']):
            
            coste_actualizado = solution['cost'] + solution['instance']['k'][i-1]
            capacidad_actualizada = solution['capacity'] + solution['instance']['b'][i-1]
            
            if (coste_actualizado <= solution['instance']['K'] and capacidad_actualizada >= solution['instance']['B']):
                
                CL.append(i)
                
    return CL
    
    
    
    
    