# Módulo con todas las funciones greedys que usamos para los distintos métodos

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


def greedyfunction_dist(solution, CL):
    
    min_distancias = []
    
    for node in CL:
        
        min_dist = calculateMinDist(node, solution)
        
        min_distancias.append(min_dist)
   
    return min_distancias


def calculateMinDist(node, solution):
    
    # Calculamos la mínima distancia del nodo con la solución
            
    distancias = [solution['instance']['m'][node-1][j-1] for j in solution['selected'] if j != node]

    min_dist = min(distancias)

    return min_dist