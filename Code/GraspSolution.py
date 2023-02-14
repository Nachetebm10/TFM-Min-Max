import random
import numpy as np
from evaluateSolution import evaluate

# Módulo que utiliza el algoritmo GRASP para crear una solución

def createGraspSolution(solution, threeshold = 0.7):
    
    # Añadimos el primer elemento al azar 
    
    first = random.randint(0, solution['instance']['n'])
    addNode(first, solution)

    # Construimos la CL
    
    print(solution['selected'])
    
    CL = constructionCL(solution)
    
    # Empezemos el algoritmo
    
    while len(CL) > 0:
        
        greedy_values = []
        
        for i in CL:
            
            greedy_values.append(greedyFunction(i, CL, solution))
            
        
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
        

    return solution

def addNode(v, solution):
    
    solution['selected'].append(v)
    
    return solution


# def isFeasible(solution):
    
#     coste, capacidad = calculoRestricciones(solution)
    
#     if(coste > solution['K'] | capacidad < solution['B']):
        
#         return False
    
#     else:
        
#         return True
    


def constructionCL(solution):
    
    # Definimos la CL
    
    CL = []
    
    # Construimos la CL para los nodos que hay en la solucion
    
    for i in np.arange(1, solution['instance']['n']+1):
        
        if (i not in solution['selected']):
            
            coste, capacidad = evaluate(solution)      
            
            coste_actualizado = coste + solution['instance']['k'][i-1]
            
            if (coste_actualizado <= solution['instance']['K']):
                
                CL.append(i)
                
    return CL
                
                

def greedyFunction(site, CL, solution, beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3):
    
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
    
                   
