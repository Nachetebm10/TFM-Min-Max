# Modulo que lee las instancias


# Creamos una funcion que lea las instancias. Para ello, tendremos el cuenta el formato en el que 
# se encuentra cada una de estas. La explicacion de este formato se encuentra en 
# 'instance.format_GDP.txt'


def ReadInstances(path):
    
    instance = {}
    
    with open(path, 'r') as f:
        
        # Guardamos el tamaño del problema
        
        instance['n'] = int(f.readline().strip())
        
        # Inicializamos la matriz de adyacencia
        
        instance['m'] = []
        
        for n in range(instance['n']):
            
            instance['m'].append([0]*instance['n'])
        
        # Calculamos el número de elementos que hay en la matriz de adyacencia
        
        len = int((instance['n']*(instance['n']-1))/2)
        
        # Leemos los elementos que compondran la matriz de adyacencia
        
        for l in range(len):
            
            line = f.readline().strip().split()
            
            # Guardamos las posiciones de la matriz y la distancia entre puntos
            
            i = int(line[0])-1
            j = int(line[1])-1
            distancia = float(line[2])
            
            # Rellenamos la matriz de adyacencia
            
            instance['m'][i][j] = distancia
                
        return instance
            
        
    
            
            
            
            
            
            
            
            
            
        
        
    
    



