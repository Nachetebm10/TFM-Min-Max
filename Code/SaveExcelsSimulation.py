# Módulos útiles ajenos al trabajo

import os
import numpy as np
import time
import pandas as pd

# Módulos creados para el trabajo

from readInstances import ReadInstances
from createSolution import createSolution
from evaluateSolution import evaluation
from Constructions import GRASPConstruction
from GreedyFunctions import greedyfunction_dist
from LocalSearchGrasp import improveLS
from AuxFunctions import isFeasible



def saveSimulation(num_instances, excel_name, method = 'GRASP', 
                   first_instance = 0, reps_construction = 100):
    
    
    # Creamos un dataframe con los datos de la simulación
        
    simulacion = pd.DataFrame()
    
    # Guardamos en una lista el nombre de todas las instancias
    
    instances = os.listdir('../instances')
    
    # Comenzamos el bucle
    
    for n in np.arange(first_instance, first_instance + num_instances):
        
        print('Ejecutando instancia: ', n)
        
        # Leemos las instancias
        
        instance = ReadInstances('../instances/' + instances[n])
        
        # Creamos una solución con el método GRASP
        
        solution = createSolution(instance)
        solution = createGraspSolution(solution)
        
        # Creamos un bucle que halle 100 veces una solución y la mejore
        
        # Nos guardaremos la mejor solución
        
        best_solution = []
        best_of = 0
    
        time_inicio = time.time()
        
        for i in range(reps_construction):
            
            time_create = time.time()
            
            solution = createSolution(instance)
            
            if(method == 'GRASP'):
                
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
    
    
    path = '../' + excel_name + '.xlsx'
    simulacion.to_excel(path, encoding = 'utf-8', index = False)
    
