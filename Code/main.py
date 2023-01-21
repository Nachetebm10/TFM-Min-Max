# Cargamos los módulos necesarios

import os
import numpy as np
from readInstances import ReadInstances

#Sacamos la lista de elementos de la carpeta instance

instancias = os.listdir('../instances')

#Leemos las instancias

instance = ReadInstances('../instances/' + instancias[0]) #De momento solo leemos una instancia


print(instance['n'])

for i in np.arange(0, instance['n']):
    
    print(instance['m'][i])

