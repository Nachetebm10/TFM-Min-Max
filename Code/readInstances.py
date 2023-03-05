# Modulo que lee las instancias

import numpy as np

# Creamos una funcion que lea las instancias. Para ello, tendremos el cuenta el formato en el que 
# se encuentra cada una de estas. La explicacion de este formato se encuentra en 
# 'instance.format_GDP.txt'


def ReadInstances(path):
    
    instance = {}
    
    with open(path, 'r') as f:
        
        # Guardamos el tamaño del problema
        
        instance['n'] = int(f.readline().strip())
        
        # Inicializamos la matriz de adyacencia (m)
        
        instance['m'] = []
        
        # Inicializamos el vector de coste (k) de cada localizacion
        
        instance['k'] = []
        
        # Inicializamos el vector de coste por unidad (cpu) de cada localizacion
        
        instance['cpu'] = []
        
        # Inicializamos el vector de capacidad (b) de cada localizacion
        
        instance['b'] = []
        
        # Inicializamos la matriz de adyacencia
        
        for n in range(instance['n']):
            
            instance['m'].append([0]*instance['n'])
        
        # Calculamos el número de elementos que hay en la matriz de adyacencia
        
        long = int((instance['n']*(instance['n']-1))/2)
        
        # Guardamos las distancias que compondran la matriz de adyacencia
        
        for l in range(long):
            
            line = f.readline().strip().split()
            
            # Guardamos las posiciones de la matriz y la distancia entre puntos
            
            i = int(line[0])-1
            j = int(line[1])-1
            distancia = float(line[2])
            
            # Rellenamos la matriz de adyacencia
            
            instance['m'][i][j] = distancia
            instance['m'][j][i] = distancia
        
        # Guardamos los vectores coste, coste por unidad y capacidad de localización
        
        for n in np.arange(0, instance['n']):
            
            line = f.readline().strip().split()
            
            # Leemos los valores de coste, coste por unidad y capacidad de cada localización
            
            c = float(line[1])
            cpu = float(line[2])
            k = float(line[3])
            
            # Guardamos los valores de coste, coste por unidad y capacidad de cada localización
            
            instance['k'].append(c)
            instance['cpu'].append(cpu)
            instance['b'].append(k)
            
            
        # Guardamos las restricciones del problema
        
        
        line = f.readline().strip().split()

        instance['K'] = float(line[0]) # Máximo coste
        instance['K2'] = float(line[1]) # Coste extra
        instance['B'] = float(line[2]) # Mínima capacidad

        return instance
            
        
    
            
            
            
            
        
            
            
        
        
    
    



