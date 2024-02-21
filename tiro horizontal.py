import matplotlib.pyplot as plt
import math

# Solicitar al usuario que ingrese la velocidad inicial y el ángulo
v0 = float(input("Ingrese la velocidad inicial (m/s): "))
angle = float(input("Ingrese el ángulo de lanzamiento (grados): "))

# Convertir el ángulo a radianes
angle_rad = math.radians(angle)

# Calcular la velocidad en los ejes X e Y
v0x = v0 * math.cos(angle_rad)
v0y = v0 * math.sin(angle_rad)

# Gravedad
g = 9.81

# Calcular el tiempo de vuelo
t_flight = 2 * v0y / g

# Calcular el alcance máximo
x_max = v0x * t_flight

# Generar puntos para los ejes X e Y
t = [i*0.01 for i in range(int(t_flight/0.01)+1)]
x = [v0x*i for i in t]
y = [v0y*i - 0.5*g*i**2 for i in t]

# Graficar los puntos
plt.figure()
plt.plot(x, y)
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.title('Lanzamiento Horizontal')

plt.grid(True)
plt.show()