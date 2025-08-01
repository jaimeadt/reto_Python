# SOLUCIONES RETO PYTHON


# EJECICIO 1:

# Tenemos dos opciones:
# Opción 1:
def contar_caracteres_1(cadena):
    """
    Función para contar el número de caracteres en una cadena dada.

    Parámetros:
    - cadena (str): La cadena de texto cuyos caracteres se contarán.

    Retorna:
    - int: El número total de caracteres en la cadena.
    """
    # Inicializa un contador en 0 para contar los caracteres
    contador = 0
    # Itera sobre cada caracter en la cadena
    for caracter in cadena:
        # Por cada iteración, incrementa el contador en 1
        contador += 1
    # Retorna el total de caracteres contados
    return contador
    
# Opción 2:
def contar_caracteres_2(cadena):
    """
    Función para contar el número de caracteres en una cadena dada.

    Parámetros:
    - cadena (str): La cadena de texto cuyos caracteres se contarán.

    Retorna:
    - int: El número total de caracteres en la cadena.
    """
    
    # Usar la función len para obtener la longitud de la cadena
    return len(cadena)

# Ejemplo de uso
# Definición de la cadena:
cadena1 = "¡Hola alumnos! Bienvenidos a clase"

# Llamada a la función contar_caracteres_1 con la cadena1 como argumento
print(contar_caracteres_1(cadena1))  # Output esperado: 34

# Llamada a la función contar_caracteres_2 con la cadena1 como argumento
print(contar_caracteres_2(cadena1))  # Output esperado: 34

# Definición de la cadena:
cadena2 = 3

# Llamada a la función contar_caracteres_1 con la cadena1 como argumento
print(contar_caracteres_1(cadena2))  # Output esperado: TypeError

# Llamada a la función contar_caracteres_2 con la cadena1 como argumento
print(contar_caracteres_2(cadena2))  # Output esperado: TypeError

# EJERCICIO 2:

def calcular_promedio(lista):
    """
    Función para calcular el promedio de una lista de números.

    Parámetros:
    - lista (list): Una lista de números de la cual se calculará el promedio.

    Retorna:
    - float: El promedio de los elementos en la lista. Si la lista está vacía, devuelve 0.
    """
    # Intentamos calcular el promedio:
    try:
        # Calcula la suma de todos los elementos en la lista
        suma_total = sum(lista)
        # Calcula el promedio dividiendo la suma total entre la cantidad de elementos en la lista
        promedio = suma_total / len(lista)
        # Retorna el promedio calculado
        return promedio
    
    # Manejamos el posible error de dividir entre 0
    except: ZeroDivisionError
    return f'ZeroDivisionError: No se puede dividir entre 0'

# Ejemplo de uso
# Definición de la lista de números:
numeros1 = [1, 2, 3, 4, 5]

# Llamada a la función calcular_promedio con la lista de números como argumento
print(calcular_promedio(numeros1))  # Output esperado: 3.0

# Definición de otra lista de números:
numeros2 = []

# Llamada a la función calcular_promedio con la lista de números como argumento
print(calcular_promedio(numeros2))  # Output esperado: No se puede dividir entre 0

# EJERCICIO 3:

def encontrar_duplicado(lista):
    """
    Función para encontrar el primer elemento duplicado en una lista dada.

    Parámetros:
    - lista (list): Una lista de elementos donde se buscará un duplicado.

    Retorna:
    - El primer elemento duplicado encontrado en la lista, o None si no se encuentra ninguno.
    """
    # Crea un conjunto vacío para almacenar los elementos únicos
    elementos_unicos = set()
    
    # Itera sobre cada elemento en la lista
    for elemento in lista:
        # Verifica si el elemento ya está en el conjunto de elementos únicos
        if elemento in elementos_unicos:
            # Si el elemento ya está en el conjunto, significa que es un duplicado
            return elemento
        else:
            # Si el elemento no está en el conjunto, agrégalo
            elementos_unicos.add(elemento)
    
    # Si no se encuentra ningún duplicado, retorna None
    return None

# Ejemplo de uso
# Definición de la lista de números:
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]

# Llamada a la función encontrar_duplicado con la lista de números como argumento
print(encontrar_duplicado(numeros1))  # Output esperado: 3

# Definición de otra lista de números:
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Llamada a la función encontrar_duplicado con la lista de números como argumento
print(encontrar_duplicado(numeros2))  # Output esperado: None

# EJERCICIO 4:

def enmascarado_datos(cadena):
    """
    Convierte una variable en string. Luego convierte todos los caracteres en '#' menos los 4 últimos.
    
    Parámetros:
    - cadena: La variable que se convertirá en una cadena de texto y cuyos caracteres se enmascararán.

    Retorna:
    - str: La cadena enmascarada, donde todos los caracteres, excepto los últimos cuatro, están enmascarados con el carácter '#'.
    """
    # Convierte la variable cadena en un string para asegurar que se pueda indexar
    cadena = str(cadena)
    
    # Crea una nueva cadena con '#' repetido la cantidad de veces que sea necesario,
    # excepto para los últimos cuatro caracteres, que se mantienen sin cambios
    return "#" * (len(cadena) - 4) + cadena[-4:]

# Ejemplo de uso
# Definición de la primera contraseña:
contraseña1 = "Micontraseña1234"

# Llamada a la función enmascarado_datos con la contraseña  como argumento
print(enmascarado_datos(contraseña1))  # Output esperado: 1234

# Definición de la segunda contraseña:
contraseña2 = 123456789

# Llamada a la función enmascarado_datos con la contraseña  como argumento
print(enmascarado_datos(contraseña2))  # Output esperado: 6789

# EJERCICIO 5:

def es_anagrama(palabra1, palabra2):
    """
    Determina si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

    Parámetros:
    - palabra1 (str): La primera palabra a comparar.
    - palabra2 (str): La segunda palabra a comparar.

    Retorna:
    - bool: True si las palabras son anagramas, False en caso contrario.
    """
    # Elimina los espacios en blanco y convierte las palabras a minúsculas para ignorar mayúsculas y minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Verifica si la longitud de las palabras es la misma
    if len(palabra1) != len(palabra2):
        return False
    
    # Ordena las letras de ambas palabras
    palabra1_sorted = sorted(palabra1)
    palabra2_sorted = sorted(palabra2)
    
    # Compara si las palabras ordenadas son iguales
    if palabra1_sorted == palabra2_sorted:
        return True
    else:
        return False

# Ejemplo de uso
palabra1 = "Roma"
palabra2 = "lana"
palabra3 = " hola"
palabra4 = "amor "

print(es_anagrama(palabra1, palabra2))  # Output esperado: False
print(es_anagrama(palabra1, palabra3))  # Output esperado: False
print(es_anagrama(palabra1, palabra4))  # Output esperado: True
print(es_anagrama(palabra2, palabra3))  # Output esperado: False
print(es_anagrama(palabra2, palabra4))  # Output esperado: False
print(es_anagrama(palabra3, palabra4))  # Output esperado: False

# EJERCICIO 6:

def buscar_nombre():
    """
    Solicita al usuario ingresar una lista de nombres y luego solicita un nombre para buscar en esa lista.
    Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario,
    se lanza una excepción.

    Parámetros:
    - No recibe parámetros.

    Retorna:
    - No retorna ningún valor.
    """
    try:
        # Inicializar una lista vacía para almacenar los nombres
        lista_nombres = []
        
        while True:
            # Convertir a minúsculas y eliminar espacios alrededor
            nombre = input("Ingrese un nombre o escriba 'fin' para finalizar: ").strip().lower()  
            # Salir del bucle si el usuario ingresa 'fin'
            if nombre == 'fin':
                break  
            
            lista_nombres.append(nombre)  # Agregar el nombre a la lista
        
        # Solicitar al usuario un nombre para buscar, convertirlo a minúsculas y eliminar espacios alrededor
        nombre_buscar = input("Ingrese un nombre para buscar en la lista: ").strip().lower()
        
        # Intentar encontrar el nombre en la lista
        if nombre_buscar in lista_nombres:  # Verifica si el nombre buscado está en la lista de nombres
            # Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            # Si el nombre no está en la lista, lanza una excepción ValueError
            raise ValueError(f"El nombre '{nombre_buscar}' no fue encontrado en la lista.")
    
    except ValueError as error:
        # Captura la excepción ValueError e imprime un mensaje con el tipo de error.
        print(error)

# Ejemplo de uso
buscar_nombre()

# EJERCICIO 7:

def fibonacci(n):
    """
    Calcula el término n de la serie de Fibonacci utilizando recursión.

    Parámetros:
    - n (int): El término de la serie de Fibonacci que se desea calcular.

    Retorna:
    - int: El término n de la serie de Fibonacci.
    """
    # Caso base: si n es 0 o 1, retorna n
    if n <= 1:
        return n
    # Caso recursivo: calcula la suma de los términos n-1 y n-2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Ejemplo de uso:
print(fibonacci(10))  # Output esperado: 55

# EJERCICIO 8:

def encontrar_puesto_empleado(nombre_completo, lista):
    """
    Función para encontrar el puesto de un empleado dado su nombre completo.

    Parámetros:
    - nombre_completo (str): El nombre completo del empleado.
    - lista (list): Una lista de diccionarios que contiene información sobre los empleados,
                    donde cada diccionario tiene claves "nombre", "apellido" y "puesto".

    Retorna:
    - str: El puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando
           que la persona no trabaja aquí.
    """
    try:
        nombre, apellido = nombre_completo.split()
    
    except:
        return f"{nombre_completo} no trabaja aquí"
    
    for elemento in lista:
        if nombre == elemento["nombre"] and apellido == elemento["apellido"]:
            return elemento["puesto"]
        
    return f"{nombre_completo} no trabaja aquí"

# Caso de uso
empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

print(encontrar_puesto_empleado("Juan García", empleados))  # Output: Secretario
print(encontrar_puesto_empleado("Mabel García", empleados))   # Output: Product Manager
print(encontrar_puesto_empleado("Isabel Martín", empleados))    # Output: CEO
print(encontrar_puesto_empleado("Alejandro", empleados))    # Output: Alejandro no trabaja aquí

# EJERCICIO 9:

# Definición de la función lambda cubo_numero que calcula el cubo de un número
cubo_numero = lambda numero: numero ** 3

# Ejemplo de uso
# Imprime el resultado de aplicar la función cubo_numero al número 1551
print(cubo_numero(1551))  # Output: 3731087151

# EJERCICIO 10:

# Definición de la función lambda resto_division que calcula el resto de la división entre dos números
resto_division = lambda x, y : x % y

# Ejemplo de uso
# Imprime el resultado de aplicar la función resto_division a los números 50 y 3
print(resto_division(50, 3))  # Output: 2

# EJERCICIO 11:

# Definición de la lista de números
lista_numeros = [24, 56, 2.3, 19, -1, 0]

# Definición de la función lambda numeros_pares que filtra los números pares de una lista
numeros_pares = list(filter(lambda x : x % 2 == 0, lista_numeros))

# Ejemplo de uso
# Imprime la lista de números pares
print(numeros_pares)  # Output: [24, 56, 0]

# EJERCICIO 12:

# Definición de la lista de números
lista_numeros = [24, 56, 2.3, 19, -1, 0]

# Definición de la función lambda numeros_suma que suma 3 a cada número de una lista
numeros_suma = list(map(lambda x: x + 3, lista_numeros))

# Ejemplo de uso
# Imprime la lista de números con 3 sumado a cada uno
print(numeros_suma)  # Output: [27, 59, 5.3, 22, 2, 3]

# EJERCICIO 13:

# Definición de las listas de números
lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]

# Definición de la función lambda sumar_listas que suma elementos correspondientes de dos listas
sumar_listas = lambda lista1, lista2: [x + y for x,y in zip(lista1, lista2)]

# Ejemplo de uso
# Imprime la lista resultante de sumar elementos correspondientes de lista_numeros_1 y lista_numeros_2
print(sumar_listas(lista_numeros_1, lista_numeros_2))  # Output: [4, 15, 39, 62]

# EJERCICIO 14:

class Arbol:
    """
    La clase Arbol modela un árbol genérico con tronco y ramas.
    """

    def __init__(self):
        """
        Inicializa un árbol con un tronco de longitud 1 y sin ramas.
        
        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Longitud inicial del tronco
        self.altura_tronco = 1  
        # Lista de ramas del árbol
        self.ramas = []  
    
    def crecer_tronco(self):
        """
        Método para hacer crecer el tronco del árbol.
        
        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Incrementa la longitud del tronco en 1
        self.altura_tronco += 1  
    
    def nueva_rama(self):
        """
        Método para añadir una nueva rama al árbol.
        
        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Agrega una nueva rama de longitud 1
        self.ramas.append(1)  
    
    def crecer_ramas(self):
        """
        Método para hacer crecer todas las ramas del árbol.
        
        Parámetros:
        - Ninguno
        
        Retorna:
        - None
        """
        # Incrementa en 1 la longitud de todas las ramas
        self.ramas = [rama + 1 for rama in self.ramas] 

    def quitar_rama(self, n):
        """
        Método para quitar una rama del árbol en la posición especificada.
        
        Parámetros:
        - n (int): Índice de la rama a quitar
        
        Retorna:
        - str: Mensaje indicando si se quitó la rama o no
        """
        # No se realiza ninguna acción si el índice es inválido
        if n <= 0 or n > len(self.ramas):
            return f"No se ha caído ninguna rama"
        # Elimina la rama en la posición n  
        else:
            del self.ramas[n]  

    def info_arbol(self):
        """
        Método para obtener información sobre el árbol.
        
        Parámetros:
        - Ninguno
        
        Retorna:
        - str: Descripción del árbol incluyendo longitud del tronco, número de ramas y longitudes de las ramas
        """
        if len(self.ramas) == 0:
            return f"El árbol tiene una longitud de {self.altura_tronco} y no tiene ninguna rama"
        else:
            info_ramas = [f"rama_{i + 1}: {longitud}" for i, longitud in enumerate(self.ramas)]
            return f"El árbol tiene una longitud de {self.altura_tronco}, tiene {len(self.ramas)} ramas, con las siguientes longitudes: {', '.join(info_ramas)}"
        
# Caso de uso:

arbol1 = Arbol()
# Hacemos crecer el arbol1 una unidad.
arbol1.crecer_tronco()

# Añadimos una nueva rama.
arbol1.nueva_rama()

# Hacemos crecer las ramas una unidad.
arbol1.crecer_ramas()

# Añadimos una nueva rama.
arbol1.nueva_rama()

# Añadimos una nueva rama.
arbol1.nueva_rama()

# Retiramos una rama en una posición concreta.
arbol1.quitar_rama(2)

# Llamamos al método que nos devuelve la descripción del árbol:
arbol1.info_arbol() # Output esperado: 'El árbol tiene una longitud de 2, tiene 2 ramas, con las siguientes longitudes: rama_1: 2, rama_2: 1'

# EJERCICIO 15:

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=False):
        """
        Inicializa un usuario con su nombre, saldo y si tiene o no cuenta corriente.

        Parámetros:
        - nombre (str): El nombre del usuario.
        - saldo (float): El saldo inicial del usuario.
        - cuenta_corriente (bool, opcional): Indica si el usuario tiene cuenta corriente o no.
                                              Por defecto es False.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, dinero):
        """
        Método para retirar dinero del saldo del usuario.

        Parámetros:
        - dinero (float): La cantidad de dinero a retirar del saldo.

        Retorna:
        - str: Un mensaje indicando el nuevo saldo del usuario.

        Lanza:
        - ValueError: Si el saldo no es suficiente para retirar la cantidad deseada.
        """
        if dinero > self.saldo:
            raise ValueError("No hay suficiente saldo para retirar.")
        self.saldo -= dinero
        return f"{self.nombre} tiene {self.saldo}."

    def transferir_dinero(self, otro_usuario, dinero):
        """
        Método para realizar una transferencia desde otro usuario al usuario actual.

        Parámetros:
        - otro_usuario (UsuarioBanco): El usuario desde el cual se realizará la transferencia.
        - dinero (float): La cantidad de dinero a transferir desde otro_usuario a self.

        Retorna:
        - str: Un mensaje indicando los nuevos saldos de ambos usuarios después de la transferencia.

        Lanza:
        - ValueError: Si otro_usuario no tiene cuenta corriente o no tiene suficiente saldo para la transferencia.
        """
        if not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if dinero > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir.")
        self.saldo += dinero
        otro_usuario.saldo -= dinero
        return f"{self.nombre} tiene {self.saldo}. {otro_usuario.nombre} tiene {otro_usuario.saldo}."

    def agregar_dinero(self, dinero):
        """
        Método para agregar dinero al saldo del usuario.

        Parámetros:
        - dinero (float): La cantidad de dinero a agregar al saldo.

        Retorna:
        - str: Un mensaje indicando el nuevo saldo del usuario.
        """
        self.saldo += dinero
        return f"{self.nombre} tiene {self.saldo}."
    
# Ejemplo de uso:
usuario1 = UsuarioBanco("Alicia", 100, cuenta_corriente=True)
usuario2 = UsuarioBanco("Bob", 50, cuenta_corriente=False)

print(usuario1.agregar_dinero(20))  # Output esperado: Alicia tiene 80.
print(usuario2.transferir_dinero(usuario1, 80))  # Output esperado: Bob tiene 130. Alicia tiene 40.
print(usuario1.retirar_dinero(50))  # Output esperado: Alicia tiene 120.
# Output esperado: ValueError

# EJERCICIO 16:

def contar_palabras(texto):
    """
    Función que cuenta la frecuencia de cada palabra en un texto dado.
    
    Parámetros:
    - texto (str): El texto del cual se contarán las palabras.
    
    Retorna:
    - dict: Un diccionario donde las claves son las palabras y los valores son las frecuencias de cada palabra.
    """
    # Inicializa un diccionario para almacenar el conteo de palabras
    conteo = {} 
    # Divide el texto en palabras y las convierte a minúsculas
    palabras = texto.lower().split()  
    for palabra in palabras:
        # Establecemos la clave-valor con palabra, 0 mediante el get. Después incrementamos en 1:
        conteo[palabra] = conteo.get(palabra, 0) + 1  
    return conteo

def reemplazar_palabra(texto, palabra_original, palabra_nueva):
    """
    Función que reemplaza una palabra original por una nueva en un texto dado.
    
    Parámetros:
    - texto (str): El texto en el cual se realizará el reemplazo.
    - palabra_original (str): La palabra que se desea reemplazar.
    - palabra_nueva (str): La palabra nueva que se utilizará para el reemplazo.
    
    Retorna:
    - str: El texto con la palabra original reemplazada por la nueva.
    """
    # Divide el texto en palabras y las convierte a minúsculas
    resultado = []
    palabras = texto.lower().split()  
    for palabra in palabras:
        if palabra == palabra_original:
            # Agrega la palabra nueva si coincide con la palabra original
            resultado.append(palabra_nueva)  
        else:
            # Conserva la palabra original si no coincide con la palabra original
            resultado.append(palabra) 

    # Une las palabras en un solo texto
    return ' '.join(resultado)  

def eliminar_palabra(texto, palabra_eliminar):
    """
    Función que elimina una palabra específica de un texto dado.
    
    Parámetros:
    - texto (str): El texto del cual se eliminará la palabra.
    - palabra_eliminar (str): La palabra que se desea eliminar del texto.
    
    Retorna:
    - str: El texto con la palabra especificada eliminada.
    """
    # Divide el texto en palabras
    palabras = texto.lower().split()  
    resultado = []
    for palabra in palabras:
        if palabra != palabra_eliminar:
            # Conserva la palabra si no coincide con la palabra a eliminar
            resultado.append(palabra)
    # Une las palabras en un solo texto  
    return ' '.join(resultado)  

def procesar_texto(texto, opcion, *args):
    """
    Función que procesa un texto según la opción especificada.
    
    Parámetros:
    - texto (str): El texto que se va a procesar.
    - opcion (str): La opción de procesamiento ("contar", "remplazar" o "eliminar").
    - *args: Argumentos adicionales dependiendo de la opción.
    
    Retorna:
    - Dependiendo de la opción:
        - Si la opción es "contar", retorna un diccionario con el conteo de palabras.
        - Si la opción es "remplazar", retorna el texto con la palabra original reemplazada por la nueva.
        - Si la opción es "eliminar", retorna el texto con la palabra especificada eliminada.
    
    Levanta:
    - ValueError: Si la opción proporcionada no es válida o si el número de argumentos es incorrecto.
    """
    if opcion == "contar":
    # Si la opción es "contar", llama a la función contar_palabras
        return contar_palabras(texto)
    elif opcion == "remplazar":
        # Si la opción es "remplazar", verifica si se proporcionaron dos argumentos
        if len(args) != 2:
            # Si no se proporcionaron dos argumentos, levanta un ValueError
            raise ValueError(f"Se esperan dos argumentos para reemplazar. Argumentos pasados: {len(args)}")
        # Si se proporcionaron dos argumentos, llama a la función reemplazar_palabra
        return reemplazar_palabra(texto, args[0], args[1])
    elif opcion == "eliminar":
        # Si la opción es "eliminar", verifica si se proporcionó un argumento
        if len(args) != 1:
            # Si no se proporcionó un argumento, levanta un ValueError
            raise ValueError(f"Se espera un argumento para eliminar. Argumentos pasados: {len(args)}")
        # Si se proporcionó un argumento, llama a la función eliminar_palabra
        return eliminar_palabra(texto, args[0])
    else:
        # Si la opción no es válida, levanta un ValueError
        raise ValueError(f"Opción no válida")

# Texto de ejemplo
texto = "Este es un ejemplo de texto . Este texto contiene palabras repetidas."

# Caso de uso para contar palabras en el texto
conteo_palabras = procesar_texto(texto, "contar")
print("Conteo de palabras en el texto:")
print(conteo_palabras)
# Output esperado:
# Conteo de palabras en el texto:
# {'este': 2, 'es': 1, 'un': 1, 'ejemplo': 1, 'de': 1, 'texto': 2, '.': 1, 'contiene': 1, 'palabras': 1, 'repetidas.': 1}

# Caso de uso para reemplazar una palabra en el texto
texto_reemplazado = procesar_texto(texto, "remplazar", "texto", "relato")
print("\nTexto con la palabra 'texto' reemplazada por 'relato':")
print(texto_reemplazado)
# Output esperado:
# Texto con la palabra 'texto' reemplazada por 'relato':
# este es un ejemplo de relato . este relato contiene palabras repetidas.

# Caso de uso para eliminar una palabra del texto
texto_sin_palabra = procesar_texto(texto, "eliminar", "ejemplo")
print("\nTexto con la palabra 'ejemplo' eliminada:")
print(texto_sin_palabra)
# Output esperado:
#Texto con la palabra 'ejemplo' eliminada:
#este es un de texto . este texto contiene palabras repetidas.
