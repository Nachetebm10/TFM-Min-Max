import random
import numpy as np
from evaluateSolution import evaluation, removeNode, addNode

# Módulo que utiliza el algoritmo GRASP para crear una solución

def createGraspSolution(solution, threeshold = 0.3):
    
    # Añadimos el primer elemento al azar 
    
    first = random.randint(0, solution['instance']['n'])
    addNode(first, solution)
    
    # Construimos la CL
    
    CL = constructionCL(solution)
    
    # Empezemos el algoritmo
    
    while len(CL) > 0:
        
        # Con la función de Anna
        
        # greedy_values = []
        
        # for i in CL:
            
        #     greedy_values.append(greedyFunction(i, CL, solution))
            
        # Con la función greedy ratio
        
        greedy_values = greedyFunction_ratio(solution, CL)
        
        # Calculamos la RCL
        
        RCL = []
        
        mu = min(greedy_values) + threeshold * (max(greedy_values) - min(greedy_values))
        
        for i in range(len(CL)):
            
                if (greedy_values[i] >= mu):
                    
                    RCL.append(CL[i])
                
        # Escogemos un valor aleatorio de la RCL
    
        node = random.choice(RCL)
        
        # Añadimos el nodo a la solución
        
        addNode(node, solution)
        
        # Volvemos a construir la CL
    
        CL = constructionCL(solution)
        
    
    # while isFeasible(solution) != True:
        
    #     # Buscamos el nodo con menor capacidad de la solución
        
    #     min_capacity_sol = 100000
    #     max_cost_sol = 0
        
    #     for node in solution['selected']:
            
    #         if (solution['instance']['b'][node-1] < min_capacity_sol and solution['instance']['k'][node-1] > max_cost_sol):
                
    #             min_capacity_sol = solution['instance']['b'][node-1]
    #             max_cost_sol = solution['instance']['k'][node-1] 
                
    #             node_min_cap_max_cost = node
        
        
    #     # Buscamos el nodo con mayor capacidad y menos coste de los que no están en la solución
        
    #     max_capacity_sol = 0
    #     min_cost_sol = 100000
        
    #     for node in set(range(solution['instance']['n'])) - set(solution['selected']):
            
    #         if (solution['instance']['b'][node-1] > max_capacity_sol and solution['instance']['k'][node-1] < min_cost_sol):
                
    #             max_capacity_sol = solution['instance']['b'][node-1]
    #             min_cost_sol = solution['instance']['k'][node-1] 
                                
                
    #             node_max_cap_min_cost = node
        
    #     # Hacemos el intercambio de nodos
        
    #     removeNode(node_min_cap_max_cost, solution)
    #     addNode(node_max_cap_min_cost, solution)
        
    #     print('b')
    #     print(isFeasible(solution))
        
    return solution



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
                
                

def greedyFunction_Anna(site, CL, solution, beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3):
    
    value = 0
    
    # Primer término de la greedy function
    
    max_dist_CL = max(map(max, [solution['instance']['m'][i-1][:] for i in CL]))
    sum_di_CL = sum([solution['instance']['m'][i-1][site-1] for i in CL])
    
    # Segundo término de la greedy function
    
    max_capacity_CL = max([solution['instance']['b'][i-1] for i in CL])
    ci = int(solution['instance']['b'][site-1])
    
    # Tercer término de la función
    
    max_cost_CL = max([solution['instance']['k'][i-1] for i in CL])
    ai = int(solution['instance']['k'][site-1])
    
    # Calculamos el valor
    
    value = beta_dist*(sum_di_CL/max_dist_CL) + beta_cap*(ci/max_capacity_CL) + beta_cost*((max_cost_CL - ai)/max_cost_CL)
    
    
    return value


def greedyFunction_ratio(solution, CL):
    
    greedy_values = [solution['instance']['b'][i-1]/solution['instance']['k'][i-1] for i in CL]
    return greedy_values

def isFeasible(solution):
    
    if ((solution['cost'] > solution['instance']['K']) or (solution['capacity'] < solution['instance']['B'])):
        
        return False
    
    else:
        return True
                   
