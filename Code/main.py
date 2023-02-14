# Cargamos los módulos necesarios

import os
import numpy as np
from readInstances import ReadInstances
from createSolution import createSolution
from GraspSolution import createGraspSolution
from evaluateSolution import evalCostCapacity, evaluation

#Sacamos la lista de elementos de la carpeta instance

instancias = os.listdir('../instances')

#Leemos las instancias

instance = ReadInstances('../instances/' + instancias[0]) #De momento solo leemos una instancia

# # Comprobamos que se lee la instancia correctamente

# ## Tamaño

# print(instance['n'])

# ## Matriz de adyacencia

# for i in np.arange(0, instance['n']):
    
#     print(instance['m'][i])

# ## Vectores de coste, coste por unidad y capacidad

# print(instance['k'])
# print(instance['cpu'])
# print(instance['b'])

# ## Restricciones

# print(instance['K'])
# print(instance['K2'])
# print(instance['B'])

solution = createSolution(instance)
solution = createGraspSolution(solution)

print(solution['selected'])

# Evaluamos la solución

evaluation(solution)

# Mostramos la función objetivo

print(solution['of'])

[coste, capacidad] = evalCostCapacity(solution)

print('El coste es ' + str(coste) + ' y la capacidad es ' + str(capacidad))





