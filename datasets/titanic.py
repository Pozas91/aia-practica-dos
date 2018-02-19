# =============================================================================
# CONJUNTO DE DATOS SACADO DEL TITANIC (titanic.txt)
# =============================================================================

import random
path = "titanic.txt"

# =============================================================================
# PROCESAMOS LOS DATOS DEL FICHERO
# =============================================================================

atributos = [("Clase",["1st","2nd","3rd"]),("Edad",["0","1","2"]),("Género",["male","female"])]

# El atributo de clasificación indica si se sobrevive o no
clasificacion = 'Supervivencia'

# Las clases representan al atributo Edad que según el corte establecido de edad representa vive (1) o muere (0)
clases = ['0', '1']

titanic_list = []

# Función utilizada para realizar asignar 0, 1 y 2 en función de la edad y su expectativa de vida
def corte_edad(edad):
    res = ""
    
    if edad == 'NA':
        edad = random.randint(1,100)
    else:
        edad = float(edad)
    
    if (edad <= 13):
        res = "0"
    elif (edad >= 60):
        res = "1"
    else:
        res = "2"
        
    return res

# Función utilizada para crear un conjunto de datos (Entrenamiento, Validación y Prueba)
def genera_ejemplos(datos, proporciones):
    
    if(sum(proporciones) != 1):
        raise ValueError("El total de las proporciones tiene que ser uno")
    
    total = len(datos)
    lista_resultante = list()
    ultimo_limite = 0
    actual = 0
    proporciones_totales = len(proporciones)
    
    for i, proporcion in enumerate(proporciones):
        
        if((i + 1) == proporciones_totales):
            lista = datos[ultimo_limite:]
        else:
            limite = int(total * proporcion) + ultimo_limite
            lista = datos[ultimo_limite:limite]
            ultimo_limite = limite
            actual += len(lista)
            
        lista_resultante.append(lista)

    return lista_resultante

# Abrimos el fichero titanic.txt para recorrer toda la información incrustada en el fichero
with open(path, "r", encoding="utf8") as file:
    
    # Ejecutamos el método next(file) para saltarnos la primera linea que incluye las cabeceras
    next(file)
    
    for line in file.readlines():
        titanic = []
        
        # Eliminamos la coma y quitamos aquellos campos que se encuentren vacios o nulos
        f_aux = line.replace(",","").split('"')
        f_aux = [x for x in f_aux if x]
        
        # Clase
        titanic.append(f_aux[1])
        
        # Supervivencia
        titanic.append(f_aux[2])
        
        # Edad
        titanic.append(corte_edad(f_aux[4]))
        
        # Género
        titanic.append(f_aux[-2])
        
        titanic_list.append(titanic)
        
    file.close()

# =============================================================================
# CONJUNTO DE ENTRENAMIENTO
# =============================================================================
ejemplos = genera_ejemplos(titanic_list, [0.6, 0.2, 0.2])
entrenamiento = ejemplos[0]

# =============================================================================
# CONJUNTO DE VALIDACIÓN
# =============================================================================
validacion = ejemplos[1]

# =============================================================================
# CONJUNTO DE PRUEBA
# =============================================================================
prueba = ejemplos[2]

# =============================================================================
# EJEMPLO
# =============================================================================

ejemplo = ['3rd', '0', '2', 'female']