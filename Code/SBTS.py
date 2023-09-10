
# Modulo que contiene las funciones para ejecutar un SBTS

import numpy as np
import copy
from evaluateSolution import addNode, removeNode
from AuxFunctions import improvementCL, NodeMinDist
import random

def SBTS(solution, moves = 10):
    
    
    # Iniciamos las variable iniciales
    
    shift = True
    move = 0
    best_solution = copy.deepcopy(solution)
    
    # Definimos las funciones Hash
    
    
    Hash_Matrix = np.zeros((3, 10**5))
    hash_functions = [0] * 3
    
    # Actualizamos la matriz Hash con la solución actual
    
    [Hash_Matrix, hash_functions] = Hash_Functions(solution, Hash_Matrix)
    
    while (move <= moves and shift == True):
        
        # Probaremos a eliminar el primero de los nodos. Si sucede el caso de que
        # de que hubiera mas de 2 nodos, eliminamos la mitad de estos nodos
        
        move += 1
        print('Move:', move)
        isCLNull = True
        NodesChecked = []
        aux_solution = copy.deepcopy(solution)
        isHashTabu = True
        
        # Buscamos los mejores nodos fuera de la solucion
               
        
        while (isHashTabu == True and shift == True):
            
            while (isCLNull == True):
            
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
                nodes_out_solution = [i for i in CL if i not in NodesChecked]
                
                if (len(nodes_out_solution) == 0):
                    
                    isCLNull = True
                    addNode(node_out, solution)

                else:
                    
                    isCLNull = False
            
            node_in = 0
            best_min_dist = 0
            
            # Calculamos cual es el mejor nodo para la solucion
            
            if (len(nodes_out_solution) != 0):
                
                for i in nodes_out_solution:
                    
                    # min_dist_in = calculateMinDist(i, solution)
                    min_dist_in = solution['dist_to_S'][i-1,0]
                    
                    if (min_dist_in > best_min_dist):
                        
                        best_min_dist = min_dist_in
                        node_in = i
                        
                                             
            
            else:
            
                shift = False
            
            
            if shift:
                
                # Anyadimos el nodo a la solucion
                    
                solution = addNode(node_in, solution)
                    
                # Comprobamos si la solucion es Tabu
                    
                [HashTabuSolution, Hash_Matrix_Possible] = HashTabu(solution, Hash_Matrix)
                    
                if (HashTabuSolution == True):
                    
                    solution = removeNode(node_in, solution)
                    solution = addNode(node_out, solution)
                    CL = CL.remove(node_in)
                    
                else:
                        
                    Hash_Matrix = Hash_Matrix_Possible
                    isHashTabu = False
            
        
        if(solution['of'] > best_solution['of']):
                
            best_solution = copy.deepcopy(solution)
        
    return best_solution



def Hash_Functions(solution, Hash_Matrix):
    
    # Definimos las beta_k
    
    beta_k = [300, 400, 500]
    
    # Inicializamos las w_k. Las metemos en una matriz, W
    
    W_Matrix = np.zeros((3, solution['instance']['n']))
    
    for j in range(3):
        
        W_Matrix[j,0] = beta_k[j]
    
    
    # Calculamos la matriz W
    
    for i in np.arange(1,solution['instance']['n']):
        
        for j in range(3):
        

            W_Matrix[j,i] = W_Matrix[j,i-1] + beta_k[j] + random.randint(0, beta_k[j]/2)
        
    # Inicializamos las funciones h_k
    
    hash_functions = [0,0,0]
    
    # Calculamos las funciones h_k
    
    for j in range(3):
        
        hash_functions[j] = sum(W_Matrix[j, np.array(solution['selected']) - 1]) % np.shape(Hash_Matrix)[1]
        hash_functions[j] = int(hash_functions[j])
        
        # Actualizamos la matriz Hash

        Hash_Matrix[j, hash_functions[j]] = 1
        
        
    return Hash_Matrix, hash_functions
        

def HashTabu(solution, Hash_Matrix):
    
    HashTabuSolution = False
    
    [Hash_Matrix_New, hash_functions_new] = Hash_Functions(solution, Hash_Matrix)
    
    if (Hash_Matrix[0,hash_functions_new[0]] == 1 and Hash_Matrix[1,hash_functions_new[1]] == 1 
        and Hash_Matrix[2,hash_functions_new[2]] == 1):
        
        HashTabuSolution == True
        
    else:
        
        HashTabuSolution == False
        
    return (HashTabuSolution, Hash_Matrix_New)
    
    
    
    
    
        
        
        
    
    
        
    
    