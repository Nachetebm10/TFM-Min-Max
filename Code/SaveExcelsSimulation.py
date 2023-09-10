# Módulos útiles ajenos al trabajo

import os
import numpy as np
import time
import pandas as pd

# Módulos creados para el trabajo

from readInstances import ReadInstances
from SolutionConstruction import SolutionConstruction
from TabuSearch import TabuSearch
from SBTS import SBTS




def saveSimulation(num_instances, path, method = 'GRASP', do_Tabu = False, do_SBTS = False,
                   first_instance = 0, reps_construction = 100, function = 'dist', beta_dist = 1/3, beta_cap = 1/3, 
                   beta_cost = 1/3, threesholdGRASP = 0.3, moves_Tabu = 10, moves_SBTS = 100):
    
    
    # Creamos un dataframe con los datos de la simulación
        
    simulacion = pd.DataFrame()
    
    # Guardamos en una lista el nombre de todas las instancias
    
    instances = os.listdir('../instances')
    
    # Comenzamos el bucle
    
    for n in np.arange(first_instance, first_instance + num_instances):
        
        print('Ejecutando instancia: ', n)
        
        # Leemos las instancias
        
        instance = ReadInstances('../instances/' + instances[n])
        
      
        # Creamos un bucle que halle 100 veces una solución y la mejore
    
        time_inicio = time.time()
        
            
        solution, feasible_at_first, feasible_before_moves = SolutionConstruction(instance, 
                                        num_constructions = reps_construction, construction_method = method,
                                        function = function, beta_dist = beta_dist, beta_cap = beta_cap, 
                                        beta_cost = beta_cost, threesholdGRASP = threesholdGRASP, show_reps = True)
    
        
        if(do_Tabu):
            
            solution = TabuSearch(solution, int(instance['n']*0.1), moves = moves_Tabu)
            
        if(do_SBTS):
            
            solution = SBTS(solution, moves = moves_SBTS)
        
        time_fin = time.time()
               
        new_row = {'Instancia': instances[n], 'Nodos': instance['n'], 'Mejor solución': solution['selected'],
         'Min Distancia': solution['of'], 'Coste': solution['cost'], 
         'Capacidad': solution['capacity'], 'Coste Max': instance['K'], 
         'Cap Min': instance['B'], 'Tiempo para Mejor': solution['time_to_best'],
         'Tiempo Total': time_fin - time_inicio, 'Factibles 1 intento': feasible_at_first, 
         'Factibles': feasible_before_moves}
        
        simulacion = simulacion.append(new_row, ignore_index = True)
    
    simulacion.to_excel(path, encoding = 'utf-8', index = False)
    
