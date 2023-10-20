# Definir el entorno como una cuadr�cula
grid = [
    [0, 0, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 1]  # El 1 representa el estado objetivo
]

# Tama�o de la cuadr�cula
rows = len(grid)
cols = len(grid[0])

# Inicializar la pol�tica aleatoriamente
policy = [["" for _ in range(cols)] for _ in range(rows)]

# Par�metro de descuento
gamma = 0.9

# Realizar la b�squeda de pol�tica iterativamente
num_iterations = 100
for _ in range(num_iterations):
    policy_stable = True  # Verificar si la pol�tica se ha vuelto estable

    # Crear una funci�n de utilidad para almacenar los valores
    utility = [[0 for _ in range(cols)] for _ in range(rows)]

    # Para cada estado en la cuadr�cula
    for x in range(rows):
        for y in range(cols):
            state = (x, y)
            if grid[x][y] == 1:  # Estado objetivo
                continue

            # Acciones posibles (arriba, abajo, izquierda, derecha)
            actions = ["up", "down", "left", "right"]
            action_values = []

            # Calcular el valor de las acciones
            for action in actions:
                if action == "up":
                    next_x, next_y = x - 1, y
                elif action == "down":
                    next_x, next_y = x + 1, y
                elif action == "left":
                    next_x, next_y = x, y - 1
                elif action == "right":
                    next_x, next_y = x, y + 1

                # Verificar si la acci�n es v�lida (dentro de la cuadr�cula)
                if 0 <= next_x < rows and 0 <= next_y < cols:
                    action_value = grid[next_x][next_y] + gamma * utility[next_x][next_y]
                    action_values.append(action_value)

            if action_values:  # Verificar si hay valores de acciones
                # Elegir la acci�n con el mayor valor
                best_action_index = action_values.index(max(action_values))
                best_action = actions[best_action_index]

                # Actualizar la pol�tica si la mejor acci�n es diferente de la pol�tica actual
                if policy[x][y] != best_action:
                    policy_stable = False
                    policy[x][y] = best_action

    # Si la pol�tica es estable, salimos temprano
    if policy_stable:
        break

# Mostrar la pol�tica �ptima
for row in policy:
    print(" ".join(row))
