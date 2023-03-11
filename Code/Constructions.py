import random
from createSolution import createSolution
from evaluateSolution import evaluation, removeNode, addNode
from GreedyFunctions import greedyfunction_dist, greedyFunction_ratio, greedyFunction_Anna
from AuxFunctions import constructionCL, isFeasible

# Función que crea una solución utilizando la función voraz que se queda en cada paso con la máxima mínima distancia

def greedyConstruction(solution):
    
    
    while not isFeasible(solution):
        
        solution = createSolution(solution['instance'])
        
        first = random.randint(0, solution['instance']['n']);
        
        addNode(first, solution)
        
        # Construimos la CL
        
        CL = constructionCL(solution)
        
        # Empezemos el algoritmo
        
            
        while len(CL) > 0:
            
            # Evaluamos la función voraz
            
            min_distancias = greedyfunction_dist(solution, CL)
            
            # Cogemos la mejor solución
            
            best_min_dist = 0
            
            for i in range(len(CL)):
                
                if(min_distancias[i] > best_min_dist):
                    
                    node_in = CL[i]
                    best_min_dist = min_distancias[i]
                    
                    
            # Añadimos el nodo a la solución
            
            addNode(node_in, solution)
            
            # Volvemos a construir la CL
        
            CL = constructionCL(solution)
        
    return solution
    


# Función que crea una solución utilizando el método GRASP

def GRASPConstruction(solution, threeshold = 0.3):
    
    # Añadimos el primer elemento al azar 
    
    first = random.randint(0, solution['instance']['n'])
    addNode(first, solution)
    
    # Construimos la CL
    
    CL = constructionCL(solution)
    
    # Empezemos el algoritmo
    
    while len(CL) > 0:
        
        # Con la función de Anna
        
        # greedy_values = []
        
        # for i in CL:
            
        #     greedy_values.append(greedyFunction(i, CL, solution))
            
        # Con la función greedy ratio
        
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
        
        addNode(node, solution)
        
        # Volvemos a construir la CL
    
        CL = constructionCL(solution)
        
        
    return solution


def RandomConstruction(solution):
    
    while not isFeasible(solution):
        
        solution = createSolution(solution['instance'])
        
        first = random.randint(0, solution['instance']['n']);
        
        addNode(first, solution)
        
        # Construimos la CL
        
        CL = constructionCL(solution)
        
        # Empezemos el algoritmo
        
        while len(CL) > 0:
            
            # Cogemos un nodo aleatorio de la CL
            
            node_in = random.choice(CL)
            
            # Añadimos el nodo a la solución
            
            addNode(node_in, solution)
            
            # Construimos la CL para la nueva solución
            
            CL = constructionCL(solution)
            
    return solution
            
            
        
        
    

