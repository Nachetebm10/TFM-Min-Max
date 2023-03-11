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
    
    
    if (isFeasible(solution) and best_solution['of'] < solution['of']):
        
        return True
    
    else:
        
        return False
         
            
                
                
        
    
    
    
    
    
    
    
    