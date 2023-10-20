import random

# Definir un entorno sencillo con dos estados y dos acciones posibles.
# El objetivo es que el agente aprenda la pol�tica �ptima mediante interacciones con el entorno.

# Definir las recompensas en el entorno.
rewards = [-1, 1]

# Hiperpar�metro de exploraci�n (probabilidad de explorar en lugar de explotar).
epsilon = 0.2

# Funci�n de valor inicializada aleatoriamente.
Q = [0, 0]

# Par�metro de descuento.
gamma = 0.9

# N�mero de episodios de aprendizaje.
num_episodes = 1000

for episode in range(num_episodes):
    state = 0  # Estado inicial
    while True:
        # Selecci�n de acci�n (exploraci�n vs. explotaci�n)
        if random.random() < epsilon:
            action = random.choice([0, 1])
        else:
            action = Q.index(max(Q))
        
        # Interacci�n con el entorno y obtenci�n de recompensa
        next_state = action
        reward = rewards[next_state]
        
        # Actualizaci�n de la funci�n de valor Q
        Q[state] += 0.1 * (reward + gamma * max(Q) - Q[state])
        
        state = next_state
        
        if state == 1:  # Estado objetivo
            break

print("Funcion de valor Q aprendida:")
print(Q)

