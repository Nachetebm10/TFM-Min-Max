# Creamos un módulo que construya una solución vacía

def createSolution(instance):
    
    solution = {}
    solution['instance'] = instance  # Guardamos la instancia
    solution['selected'] = []  # Localizaciones que seleccionaremos
    solution['of'] = 0  # Valor de la función objetivo de la solución
    
    return solution