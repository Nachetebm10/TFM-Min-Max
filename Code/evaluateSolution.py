# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:22:05 2023

@author: Ignacio
"""

import numpy as np

def removeNode(node, solution):
    
    # Eliminamos un nodo de la solución
    
    solution['selected'].remove(node)
    
    # Actualizamos la capacidad y el coste
    
    solution['cost'] -= solution['instance']['k'][node-1]
    solution['capacity'] -= solution['instance']['b'][node-1]
    
    # Actualizamos la matriz de distancias
    
    solution = UpdateDistToS(node, solution, action = 'remove')

    
    # Actualizamos la función objtetivo
    
    if(solution['of'] == solution['dist_to_S'][node-1,0]):
        
        nodes_solution = [i-1 for i in solution['selected']]
        solution['of'] = min(solution['dist_to_S'][nodes_solution, 0])
        
        if(len(solution['critical']) == 1):
            solution['critical'] = [[node, np.argmin(solution['dist_to_S'][nodes_solution, 0])+1]]
        
        else:
            
            solution['critical'].append([node, np.argmin(solution['dist_to_S'][nodes_solution, 0])+1])
    
    return solution

def addNode(node, solution):
    
    solution['selected'].append(node)
    
    # Calculamos el coste y la capacidad de la solución
    
    solution['cost'] += solution['instance']['k'][node-1]
    solution['capacity'] += solution['instance']['b'][node-1]
    
    # Actualizamos la matriz de distancias
    
    solution = UpdateDistToS(node, solution, action = 'add')
    
    
    # Actualizamos la función objetivo y los nodos críticos
    
    if(len(solution['selected']) == 1):
        
        solution['of'] = 300
    
    if(len(solution['selected']) > 1):
        

        if(solution['of'] > solution['dist_to_S'][node-1,0]):
            
            solution['of'] = solution['dist_to_S'][node-1,0]
            solution['critical'] = [ [node, solution['dist_to_S'][node-1,1]] ]
            
        elif (solution['of'] == solution['dist_to_S'][node-1,0]):
            
            solution['critical'].append([node, solution['dist_to_S'][node-1,1]])
    

    
    return solution


def UpdateDistToS(node, solution, action):
    
    if(action == 'add'):
        
        if(len(solution['selected']) == 1):
            
             # Calculamos la distancias a la solución
             
             
             solution['dist_to_S'][:,0] = solution['instance']['m'][:][node-1]
             solution['dist_to_S'][node-1,0] = 400
             solution['dist_to_S'][:,1] = node
             
             
        else:

            
            # Actualizamos la lista para los nodos fuera de la solución
            
            nodes_updates = [i for i in range(solution['instance']['n'])
                             if i != node-1 and solution['dist_to_S'][i,0] > solution['instance']['m'][i][node-1]]
            
            for node_update in nodes_updates:
                
                solution['dist_to_S'][node_update, 0] = solution['instance']['m'][node_update][node-1]
                solution['dist_to_S'][node_update, 1] = node
                
    elif(action == 'remove'):
        
         nodes_updates = [i for i in range(solution['instance']['n'])
                          if i != node-1 and solution['dist_to_S'][i,1] == node]
         
         # Calculamos la distancia a la solución
         
         if (len(solution['selected']) > 0):
             
             for node_update in nodes_updates:
               
                 
                 distancias = [solution['instance']['m'][i-1][node_update] for i in solution['selected'] 
                               if i-1 != node_update]
                 
                 solution['dist_to_S'][node_update,0] = min(distancias)
                 solution['dist_to_S'][node_update,1] = solution['selected'][np.argmin(distancias)]+1
         
    
    return solution
        
        
        
        
    
    
        