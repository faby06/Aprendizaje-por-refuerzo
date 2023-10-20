import numpy as np

# Definir el número de estados y acciones
num_estados = 6
num_acciones = 3

# Definir la matriz Q con ceros
Q = np.zeros((num_estados, num_acciones))

# Definir los parámetros de aprendizaje
tasa_aprendizaje = 0.8
factor_descuento = 0.95
num_episodios = 1000

# Definir la función para elegir una acción epsilon-greedy
def seleccionar_accion(estado, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(num_acciones)
    else:
        return np.argmax(Q[estado, :])

# Ejecutar el algoritmo Q-Learning
for episodio in range(num_episodios):
    estado = 0  # Estado inicial
    terminado = False

    while not terminado:
        epsilon = 0.3  # Valor de epsilon-greedy
        accion = seleccionar_accion(estado, epsilon)
        
        # Simular la acción y obtener la recompensa y el próximo estado
        if accion == 0:
            nuevo_estado = estado - 1
        elif accion == 1:
            nuevo_estado = estado + 1
        else:
            nuevo_estado = estado
        
        recompensa = 0  # La recompensa puede ser ajustada según el entorno
        
        # Actualizar la matriz Q
        Q[estado, accion] = Q[estado, accion] + tasa_aprendizaje * (recompensa + factor_descuento * np.max(Q[nuevo_estado, :]) - Q[estado, accion])
        
        estado = nuevo_estado
        
        if estado == num_estados - 1:
            terminado = True

print("Matriz Q aprendida:")
print(Q)
