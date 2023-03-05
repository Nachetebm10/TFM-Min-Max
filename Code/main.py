# Cargamos los módulos necesarios

import os
import numpy as np
from readInstances import ReadInstances
from createSolution import createSolution
from GraspSolution import createGraspSolution, isFeasible
from evaluateSolution import evaluation
from LocalSearchGrasp import improveLS
import time
import pandas as pd

# Creamos un dataframe con los datos de la simulación
    
simulacion = pd.DataFrame()


num_instances = 2  # Número de instancias que queremos simular

for n in np.arange(51,71):
    
    print(n)
    
    # Sacamos la lista de elementos de la carpeta instance
    
    instances = os.listdir('../instances')
    
    # Leemos las instancias
    
    instance = ReadInstances('../instances/' + instances[n]) # De momento solo leemos una instancia
    
    # Creamos una solución con el método GRASP
    
    solution = createSolution(instance)
    solution = createGraspSolution(solution)
    
    # Creamos un bucle que halle 100 veces una solución y la mejore
    
    # Nos guardaremos la mejor solución
    
    best_solution = []
    best_of = 0

    time_inicio = time.time()
    
    for i in range(100):
        
        time_create = time.time()
        
        solution = createSolution(instance)
        createGraspSolution(solution)
        improveLS(solution)
        
        if (isFeasible(solution) and best_of < solution['of']):
            
            best_solution = solution
            best_of = solution['of']
            time_best = time.time()
            
            best_solution['time_to_best'] = time_best - time_create
    
    time_fin = time.time()
           
    new_row = {'Instancia': instances[n], 'Nodos': instance['n'], 'Mejor solución': best_solution['selected'],
     'Min Distancia': best_solution['of'], 'Coste': solution['cost'], 
     'Capacidad': solution['capacity'], 'Coste Max': instance['K'], 
     'Cap Min': instance['B'], 'Tiempo para Mejor': best_solution['time_to_best'],
     'Tiempo Total': time_fin - time_inicio}
    
    simulacion = simulacion.append(new_row, ignore_index = True)


simulacion.to_excel('../simulacion_2.xlsx', encoding = 'utf-8', index = False)



