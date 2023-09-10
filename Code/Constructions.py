import random
from createSolution import createSolution
from evaluateSolution import removeNode, addNode
from GreedyFunctions import greedyFunction_dist, greedyFunction_ratio, greedyFunction_mix, greedyFunction_capacity, greedyFunction_retroactive
from AuxFunctions import constructionCL, isFeasible

# Función que crea una solución utilizando la función voraz que se queda en cada paso con la máxima mínima distancia

def greedyConstruction(solution, feasible_at_first, feasible_before_moves, function = 'dist',  beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, 
                       beta_dist_retro = 1, beta_ratio = 0):
    
    moves = 0
    
    while not isFeasible(solution):
        
        solution = createSolution(solution['instance'])

        first = random.randint(0, solution['instance']['n'])
        
        solution = addNode(first, solution)
        
        # Construimos la CL
        
        CL = constructionCL(solution)
        
        
        # Empezemos el algoritmo
        
        while len(CL) > 0:
            
            
            # Evaluamos la función voraz
            
            if(moves <= 10 and function == 'dist'):
                
                greedy_values = greedyFunction_dist(solution, CL)
            
            elif(moves <= 10 and function == 'mix'):
                
                greedy_values = greedyFunction_mix(solution, CL, beta_dist = beta_dist, beta_cap = beta_cap, 
                                                   beta_cost = beta_cost)
                
            elif(moves <= 10 and function == 'retroactive'):
                
                greedy_values = greedyFunction_retroactive(solution, CL, beta_dist = beta_dist_retro, 
                                                           beta_ratio = beta_ratio)
                
            else:
                
                greedy_values = greedyFunction_ratio(solution, CL)

                
            # Cogemos la mejor solución
            
            best_min_dist = 0
            
            
            for i in range(len(CL)):
                
                if(greedy_values[i] > best_min_dist):
                    
                    
                    node_in = CL[i]
                    best_min_dist = greedy_values[i]
                    
        
            # Añadimos el nodo a la solución
            
            solution = addNode(node_in, solution)
            
            # Volvemos a construir la CL
        
            CL = constructionCL(solution)
        
        moves = moves + 1
        
        # Actualizamos los betas de la función retroactiva
        
        if(moves <= 5):
            
            beta_dist_retro = beta_dist_retro - 0.2
            beta_ratio = beta_ratio + 0.2
            
        else:
            
            beta_dist_retro = 0
            beta_ratio = 1
        
    if(moves == 1):
        
        feasible_at_first = feasible_at_first + 1
        feasible_before_moves = feasible_before_moves + 1
        
    elif(moves > 1 and moves <= 11):
        
        feasible_before_moves = feasible_before_moves + 1
    
    return solution, feasible_at_first, feasible_before_moves
    


# Función que crea una solución utilizando el método GRASP

def GRASPConstruction(solution, feasible_at_first, feasible_before_moves, function = 'dist', beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3,
                      threeshold = 0.3, beta_dist_retro = 1, beta_ratio = 0):
    
    moves = 0
    
    while not isFeasible(solution):
        
        # Añadimos el primer elemento al azar 
        
        solution = createSolution(solution['instance'])
        first = random.randint(0, solution['instance']['n'])
        solution = addNode(first, solution)
        
        # Construimos la CL
        
        CL = constructionCL(solution)
        
        # Empezemos el algoritmo
        
        while len(CL) > 0:
            
                
            if(moves <= 10 and function == 'dist'):
                
                greedy_values = greedyFunction_dist(solution, CL)
            
            elif(moves <= 10 and function == 'mix'):
                
                greedy_values = greedyFunction_mix(solution, CL, beta_dist = beta_dist, beta_cap = beta_cap, 
                                                   beta_cost = beta_cost)
                
            elif(moves <= 10 and function == 'retroactive'):
                
                greedy_values = greedyFunction_retroactive(solution, CL, beta_dist = beta_dist_retro, 
                                                           beta_ratio = beta_ratio)
                
            else:
                
                greedy_values = greedyFunction_ratio(solution, CL)
            
            # Calculamos la RCL
            
            RCL = []
            
            mu = min(greedy_values) + threeshold * (max(greedy_values) - min(greedy_values))
            
            for i in range(len(CL)):
                
                    if (greedy_values[i] >= mu):
                        
                        RCL.append(CL[i])
                    
            # Escogemos un valor aleatorio de la RCL
        
            node = random.choice(RCL)
            
            # Añadimos el nodo a la solución
            
            solution = addNode(node, solution)
            
            # Volvemos a construir la CL
        
            CL = constructionCL(solution)
            
        moves = moves + 1
        
        # Actualizamos los betas de la función retroactiva
        
        if(moves <= 5):
            
            beta_dist_retro = beta_dist_retro - 0.2
            beta_ratio = beta_ratio + 0.2
            
        else:
            
            beta_dist_retro = 0
            beta_ratio = 1
        
    
    if(moves == 1):
        
        feasible_at_first = feasible_at_first + 1
        feasible_before_moves = feasible_before_moves + 1
        
    elif(moves > 1 and moves <= 11):
        
        feasible_before_moves = feasible_before_moves + 1
        
    return solution, feasible_at_first, feasible_before_moves


def RandomConstruction(solution, feasible_at_first, feasible_before_moves):
    
    moves = 0
    
    while (isFeasible(solution) == False or solution['of'] <= 0):
        
        
        solution = createSolution(solution['instance'])
        
        first = random.randint(0, solution['instance']['n']);
        
        solution = addNode(first, solution)
        
        # Construimos la CL
        
        CL = constructionCL(solution)
        
        # Empezemos el algoritmo
        
        if moves <= 10:
            

            while len(CL) > 0:
                
            
                # Cogemos un nodo aleatorio de la CL
                
                node_in = random.choice(CL)
                
                solution = addNode(node_in, solution)
                
                # Construimos la CL para la nueva solución
                
                CL = constructionCL(solution)
                

        
        elif (moves > 10 and moves <= 50):
            
            while len(CL) > 0:
                
                min_distancias = greedyFunction_ratio(solution, CL)

                # Cogemos la mejor solución
                
                best_min_dist = 0
                    
                    
                for i in range(len(CL)):
                        
                    if(min_distancias[i] > best_min_dist):
                            
                        node_in = CL[i]
                        best_min_dist = min_distancias[i]
                
                # Añadimos el nodo a la solución
                
                solution = addNode(node_in, solution)
                
                # Construimos la CL para la nueva solución
                
                CL = constructionCL(solution)
                
        else:
                
             while len(CL) > 0:
             

                 min_distancias = greedyFunction_capacity(solution, CL)
                     
                 # Cogemos la mejor solución
                 
                 best_min_dist = 0
                     
                     
                 for i in range(len(CL)):
                         
                     if(min_distancias[i] > best_min_dist):
                             
                         node_in = CL[i]
                         best_min_dist = min_distancias[i]
                 
                 # Añadimos el nodo a la solución
                 
                 solution = addNode(node_in, solution)
                 
                 # Construimos la CL para la nueva solución
                 
                 CL = constructionCL(solution)   
                 

        moves = moves + 1
        
    if(moves == 1):
        
        feasible_at_first = feasible_at_first + 1
        feasible_before_moves = feasible_before_moves + 1
        
    elif(moves > 1 and moves <= 11):
        
        feasible_before_moves = feasible_before_moves + 1

    return solution, feasible_at_first, feasible_before_moves
            
            
        
        
    

