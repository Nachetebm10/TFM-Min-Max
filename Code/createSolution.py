import numpy as np

# Creamos un módulo que construya una solución vacía

def createSolution(instance):
    
    solution = {}
    solution['instance'] = instance  # Guardamos la instancia
    solution['selected'] = []  # Localizaciones que seleccionaremos
    solution['of'] = 0  # Valor de la función objetivo de la solución
    solution['critical'] = []
    solution['cost'] = 0
    solution['capacity'] = 0
    solution['time_to_best'] = 0
    solution['dist_to_S'] = np.zeros((instance['n'], 2))

    
    return solution