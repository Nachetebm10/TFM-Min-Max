# -*- coding: utf-8 -*-


import random
from SaveExcelsSimulation import saveSimulation

# Para que las simulaciones se guarden correctamente, hay que crear una carpeta 'Simulaciones' al mismo
# nivel que la carpeta que contiene el código. Dentro de la carpeta simulaciones, crear una carpeta con el nombre de cada
# simulación, el cual se puede encontrar en la definición de la variables path

# Fijamos la semilla

random.seed(123456789)


# Experimento para hallar la mejor combinación de beta's para la función DistCapCostGreedyFunction:

betas = [[1/3, 1/3, 1/3], [1/2, 1/4, 1/4], [3/4, 1/8, 1/8]]

for beta in betas:
    
    print(50)
    excel_name = ('GRASP 50 ' + str(beta[0]) + ' ' + str(beta[1]) + ' ' + str(beta[2]))
    path = '../Simulaciones/Betas/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 0, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 100, function = 'mix',
                                beta_dist = beta[0], beta_cap = beta[1], beta_cost = beta[2], threesholdGRASP = 0.5)
    
    print(150)
    excel_name = ('GRASP 150 ' + str(beta[0]) + ' ' + str(beta[1]) + ' ' + str(beta[2]))
    path = '../Simulaciones/Betas/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 40, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 75, function = 'mix',
                                beta_dist = beta[0], beta_cap = beta[1], beta_cost = beta[2], threesholdGRASP = 0.5)
    
    print(500)
    excel_name = ('GRASP 500 ' + str(beta[0]) + ' ' + str(beta[1]) + ' ' + str(beta[2]))
    path = '../Simulaciones/Betas/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 80, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 10, function = 'mix',
                                beta_dist = beta[0], beta_cap = beta[1], beta_cost = beta[2], threesholdGRASP = 0.5)


# Experimento para hallar la mejor función greedy
                

functions = ['dist', 'mix', 'retroactive']

for fun in functions:
    
    print(50)
    excel_name = ('GRASP 50 ' + fun)
    path = '../Simulaciones/Funcion_Greedy/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 0, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 100, function = fun,
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.5)
    
    print(150)
    excel_name = ('GRASP 150 ' + fun)
    path = '../Simulaciones/Funcion_Greedy/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 40, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 75, function = fun,
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.5)
    
    
    print(500)
    excel_name = ('GRASP 500 ' + fun)
    path = '../Simulaciones/Funcion_Greedy/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 80, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 10, function = fun,
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.5)



# Experimento para hallar el mejor GRASP (beta's y threeshold) y el mejor Greedy


threesholds = [0.4, 0.5, 0.6, 0.7]

for threeshold in threesholds:
    
    print(50)
    excel_name = ('GRASP 50 ' + str(threeshold))
    path = '../Simulaciones/Threeshold/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 0, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 100, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = threeshold)
    
    print(150)
    excel_name = ('GRASP 150 ' + str(threeshold))
    path = '../Simulaciones/Threeshold/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 40, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 75, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = threeshold)
    
    print(500)
    excel_name = ('GRASP 500 ' + str(threeshold))
    path = '../Simulaciones/Threeshold/' + excel_name + '.xlsx'
    
    saveSimulation(4, path, first_instance = 80, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 10, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = threeshold)
                
        


# Experimento para hallar el mejor Tabu Search




methods = ['GRASP', 'Greedy', 'Random']


for method in methods:
    
    
    print(50)
    excel_name = (method + ' 50 ')
        
    path = '../Simulaciones/Tabu/' + excel_name + '.xlsx'
        
    saveSimulation(4, path, first_instance = 0, method = method, do_Tabu = True, do_SBTS = False, reps_construction = 50, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 500)
        
    print(150)
    excel_name = (method + ' 150 ')
        
    path = '../Simulaciones/Tabu/' + excel_name + '.xlsx'
        
    saveSimulation(4, path, first_instance = 40, method = method, do_Tabu = True, do_SBTS = False, reps_construction = 25, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 300)
        
    print(500)
    excel_name = (method + ' 500 ')
        
    path = '../Simulaciones/Tabu/' + excel_name + '.xlsx'
        
    saveSimulation(4, path, first_instance = 80, method = method, do_Tabu = True, do_SBTS = False, reps_construction = 5, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 250)



    
# Experimento para hallar el mejor método


# print(50)

# GRASP

excel_name = ('GRASP 50')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 0, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 150, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)

# TABU

excel_name = ('TABU 50')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 0, method = 'GRASP', do_Tabu = True, do_SBTS = False, reps_construction = 100, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)

# SBTS 

excel_name = ('SBTS 50')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 0, method = 'GRASP', do_Tabu = False, do_SBTS = True, reps_construction = 100, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)


        
print(150)

# GRASP

excel_name = ('GRASP 150')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 40, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 100, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)

# TABU

excel_name = ('TABU 150')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 40, method = 'GRASP', do_Tabu = True, do_SBTS = False, reps_construction = 50, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)

# SBTS 

excel_name = ('SBTS 150')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 40, method = 'GRASP', do_Tabu = False, do_SBTS = True, reps_construction = 50, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 400, moves_SBTS = 400)


        
print(500)

# GRASP

excel_name = ('GRASP 500')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 80, method = 'GRASP', do_Tabu = False, do_SBTS = False, reps_construction = 5, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)

# TABU

excel_name = ('TABU 500')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 80, method = 'GRASP', do_Tabu = True, do_SBTS = False, reps_construction = 3, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 100, moves_SBTS = 400)

# SBTS 

excel_name = ('SBTS 500')

path = '../Simulaciones/Mejor_Metodo/' + excel_name + '.xlsx'
        
saveSimulation(40, path, first_instance = 80, method = 'GRASP', do_Tabu = False, do_SBTS = True, reps_construction = 3, function = 'retroactive',
                                beta_dist = 1/3, beta_cap = 1/3, beta_cost = 1/3, threesholdGRASP = 0.7, moves_Tabu = 200, moves_SBTS = 400)



