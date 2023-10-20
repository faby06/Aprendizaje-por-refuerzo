import random

# Hiperpar�metro ? (probabilidad de exploraci�n).
epsilon = 0.2

# Funci�n de valor de acciones (en este caso, valores arbitrarios).
action_values = [0.2, 0.5, 0.8, 0.1]

def choose_action():
    if random.random() < epsilon:
        # Exploraci�n: selecci�n aleatoria de una acci�n.
        return random.choice(range(len(action_values)))
    else:
        # Explotaci�n: selecci�n de la acci�n con el valor m�s alto.
        return action_values.index(max(action_values))

# Ejemplo de uso:
action = choose_action()
print("Accion seleccionada:", action)

