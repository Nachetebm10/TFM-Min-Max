def evaluate(solution):
    
    # Calculamos el coste y la capacidad de la solución
    
    coste = 0
    capacidad = 0

    for i in solution['selected']:
        
        coste += solution['instance']['k'][i-1]
        capacidad += solution['instance']['b'][i-1]
        
    return (coste, capacidad)
        