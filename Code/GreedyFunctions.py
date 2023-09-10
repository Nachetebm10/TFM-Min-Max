# Módulo con todas las funciones greedys que usamos para los distintos métodos

def greedyFunction_mix(solution, CL, beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3):
    
    value = 0
    greedy_values = []
    
    max_dist_CL = max([solution['dist_to_S'][i-1,0] for i in CL])
    max_capacity_CL = max([solution['instance']['b'][i-1] for i in CL])
    max_cost_CL = max([solution['instance']['k'][i-1] for i in CL])
    
    for node in CL:
        
        # Primer término de la greedy function

        
        di_CL = solution['dist_to_S'][node-1,0]
        
        # Segundo término de la greedy function
        
        
        ci = int(solution['instance']['b'][node-1])
        
        # Tercer término de la función
        
        
        ai = int(solution['instance']['k'][node-1])
        
        # Calculamos el valor
        
        value = beta_dist*(di_CL/max_dist_CL) + beta_cap*(ci/max_capacity_CL) + beta_cost*((max_cost_CL - ai)/max_cost_CL)
        
        greedy_values.append(value)
    
    return greedy_values


def greedyFunction_ratio(solution, CL):
    
    greedy_values = [solution['instance']['b'][i-1]/solution['instance']['k'][i-1] for i in CL]
    return greedy_values

def greedyFunction_capacity(solution, CL):
    
    greedy_values = [solution['instance']['b'][i-1] for i in CL]
    return greedy_values

def greedyFunction_dist(solution, CL):
    
    min_distancias = []
    
    for node in CL:
        
        min_dist = solution['dist_to_S'][node-1,0]
        
        min_distancias.append(min_dist)
   
    return min_distancias

def greedyFunction_retroactive(solution, CL, beta_dist = 1, beta_ratio = 0):
    
    value = 0
    greedy_values = []
    
    # Max y Min de la distancias
    
    max_dist_CL = max([solution['dist_to_S'][i-1,0] for i in CL])
    min_dist_CL = min([solution['dist_to_S'][i-1,0] for i in CL])
    
    resta_min_max_dist = max_dist_CL - min_dist_CL
    
    if(resta_min_max_dist == 0):
        
        resta_min_max_dist = max_dist_CL

    
    # Max y Min del ratio
    
    max_ratio = max([solution['instance']['b'][i-1]/solution['instance']['k'][i-1] for i in CL])
    min_ratio = min([solution['instance']['b'][i-1]/solution['instance']['k'][i-1] for i in CL])
    resta_min_max_ratio = max_ratio - min_ratio

    if(resta_min_max_ratio == 0):
        
        resta_min_max_ratio = max_ratio
        
    
    
    for node in CL:
        
        # Término de la distancia
        
        di = solution['dist_to_S'][node-1,0]
        di_norm = (di-min_dist_CL)/resta_min_max_dist
        
        
        # Término del ratio entre capacidad y coste
        
        ri = solution['instance']['b'][node-1]/solution['instance']['k'][node-1]
        ri_norm = (ri - min_ratio)/resta_min_max_ratio
        
        # Calculamos el valor greedy del nodo
        
        value = beta_dist*di_norm + beta_ratio*ri_norm
        
        greedy_values.append(value)
        
    return greedy_values
        


def calculateMinDist(node, solution):
    
    # Calculamos la mínima distancia del nodo con la solución
            
    # distancias = [solution['instance']['m'][node-1][j-1] for j in solution['selected'] if j != node]
    
    nodes_solution = [i-1 for i in solution['selected']]
    min_dist = min(solution['dist_to_S'][nodes_solution, 0])

    return min_dist