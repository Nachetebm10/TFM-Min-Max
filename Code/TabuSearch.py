# Modulo que contiene las funciones para ejecutar un Tabu Search

import numpy as np
import copy
import random
from evaluateSolution import addNode, removeNode
from AuxFunctions import improvementCL, NodeMinDist, improvementCL

# Funcion que ejecuta el algoritmo Tabu Search

def TabuSearch(solution, len_tabu_list, moves = 10):

    # Definimos las lista Tabu
    
    tabu_list = [0]*len_tabu_list
    best_solution = copy.deepcopy(solution)

    # Para realizar los cambios, lo que haremos sera cambiar el que menos distancia
    # tiene respecto toda la solucion y cambiarlo por el que mas distancia tiene
    # dentro de la CL.

    # Por tanto, hallamos aquellos nodos donde esta la minima distancia
    
    move = 0
    shift =  True
    
    while (move <= moves and shift == True):
        

        # Probaremos a eliminar el primero de los nodos. Si sucede el caso de que
        # de que hubiera mas de 2 nodos, eliminamos la mitad de estos nodos
        
        isCLNull = True
        NodesChecked = []
        aux_solution = copy.deepcopy(solution)
        
        while (isCLNull == True):
            
            if(len(aux_solution['selected']) == 1):
                
                isCLNull = False
                shift = False
                
            else:
                
                # Eliminamos de la solucion auxiliar los nodos que hemos visitado
                
                if (len(NodesChecked) > 0):
                    
                    for node_checked in NodesChecked:
                        
                        if (node_checked in aux_solution['selected']):
                            
                            
                            aux_solution = removeNode(node_checked, aux_solution)
                            
                        else:
                            pass
                        
                nodes_out = NodeMinDist(aux_solution)
                node_out = random.choice(nodes_out)
                NodesChecked.append(node_out)
                solution = removeNode(node_out, solution)
                CL = improvementCL(solution)
                nodes_out_solution = [i for i in CL if i not in tabu_list and i not in NodesChecked]
                
                if (len(nodes_out_solution) == 0):
                    
                    isCLNull = True
                    addNode(node_out, solution)
    
                else:
                    
                    isCLNull = False
                    
            
        if (shift == False):
            
            pass
        
        else:
        
            # Anyadimos el nodo a la lista Tabu
            
            tabu_list = addTabuList(node_out, tabu_list)
            nodes_out_solution = [i for i in CL if i not in tabu_list]
            
            # Comprobamos si hay algún nodo fuera de la solucion que mejore a esta
            
            node_in = 0
            best_min_dist = 0
            
            
            # Calculamos cual es el mejor nodo para la solucion
            
            if (len(nodes_out_solution) != 0):
                
                for i in nodes_out_solution:
                    
                    min_dist_in = solution['dist_to_S'][i-1,0]
                    
                    if (min_dist_in > best_min_dist):
                        
                        best_min_dist = min_dist_in
                        node_in = i
            
            else:
            
                shift = False
            
            
            # Anyadimos el nodo de la CL que mejora (o que menos empeora a la
            # solucion)
            
            if shift:
                
                solution = addNode(node_in, solution)
            
            
            move += 1
            print('Move:', move)
            
            if(solution['of'] > best_solution['of']):
                
                best_solution = copy.deepcopy(solution)
            
    return best_solution



def addTabuList(node, tabu_list):
    
    new_tabu_list = []
    new_tabu_list.append(node)
    
    for l in range(len(tabu_list)-1):
        
        new_tabu_list.append(tabu_list[l])
        
    return new_tabu_list
        
        
