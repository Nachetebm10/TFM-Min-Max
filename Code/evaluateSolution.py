# Función que evalua la solucion

def evaluation(solution):
    
    # Calculamos la función objetivo
    
    min_dist = 1000000000
    
    if (len(solution['selected']) > 1):
        
        for i in solution['selected']:
            
            distancias = [solution['instance']['m'][i-1][j-1] for j in solution['selected'] if j != i]
                    
            if (min(distancias) < min_dist):
                    
                min_dist = min(distancias)
        
        solution['of'] = min_dist
    
    else:
        
        solution['of'] = 100000
    
    # Calculamos el coste y la capacidad de la solución
    
    solution['cost'] = 0
    solution['capacity'] = 0
    
    for i in solution['selected']:
        
        solution['cost'] += solution['instance']['k'][i-1]
        solution['capacity'] += solution['instance']['b'][i-1]
        

    # Calculamos los nodos críticos
    
    solution['critical'] = [0] * solution['instance']['n']
    
    if (len(solution['selected']) > 1):
    
        for i in solution['selected']:
    
        
            distancias = [solution['instance']['m'][i-1][j-1] for j in solution['selected'] if j != i]
                 
            min_dist = min(distancias)
                
            critical_nodes = [solution['selected'][j] for j in range(len(solution['selected'])) if min_dist == solution['instance']['m'][i-1][solution['selected'][j] - 1]]
                
            solution['critical'][i-1] = critical_nodes
        
        
    return solution
    

def removeNode(node, solution):
    
    # Eliminamos un nodo de la solución
    
    solution['selected'].remove(node)
    
    # Actualizamos la solucion
    
    solution = evaluation(solution)
    
    return solution

def addNode(node, solution):
    
    solution['selected'].append(node)
    
    solution['selected'] = sorted(solution['selected'])
    
    solution = evaluation(solution)
    
    return solution
        
        
    
    
        