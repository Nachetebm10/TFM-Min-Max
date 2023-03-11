# Módulos útiles ajenos al trabajo

import os

# Módulos creados para el trabajo

from readInstances import ReadInstances
from LocalSearchGrasp import improveLS
from SaveExcelsSimulation import saveSimulation
from SolutionConstruction import SolutionConstruction


# Comienzo del código

# Leemos las instancias que vamos a usar

instances = os.listdir('../instances')
instance = ReadInstances('../instances/' + instances[0])


# Creamos una solución usando la funcion SolutionConstruction. Esta función tiene
# varios parámetros, entre ellos el método que se usa para construir la solución.
# Por defecto, utilizará el metodo greedy, pero tiene las siguientes opciones:
# 'Greedy', 'GRASP' y 'Random' 


solution = SolutionConstruction(instance, num_constructions = 100, 
                                construction_method = 'Random')

# Sacamos por pantalla la mejor solución

print('Mejor solucion')
print('OF: ', solution['of'], ' Cap: ', solution['capacity'], ' Min Cap:', 
      instance['B'])


# Guardamos la simulacion

# saveSimulation(1, "prueba")

