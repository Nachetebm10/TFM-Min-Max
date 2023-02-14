# Función que calcula el coste y la capacidad de la solución

def evalCostCapacity(solution):
    
    coste = 0
    capacidad = 0

    for i in solution['selected']:
        
        coste += solution['instance']['k'][i-1]
        capacidad += solution['instance']['b'][i-1]
        
    return (coste, capacidad)


# Función que calcula la funcion objetivo de la solucion

def evaluation(solution):
    
    min_dist = 1000000000
    
    for i in solution['selected']:
        
        distancias = []
        
        distancias = [solution['instance']['m'][i-1][j-1] for j in solution['selected'] if j != i]
                
        if (min(distancias) < min_dist):
                
            min_dist = min(distancias)
    
    solution['of'] = min_dist
    
    return solution
    
        