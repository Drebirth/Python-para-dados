# Adicionando Grid Lines
# com pyplot, podemos usar grid() para adicionar linhas de grid

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,333])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.grid()
plt.show()

# Specify Which Grid Lines to Display
# podemos usar o axis paramentro no grid() para especificar as linhas no display
# valores são: 'x', 'y', e 'both'. Por padrão é 'both'

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)

plt.grid(axis='y')
plt.show()

# definir propriedades de linhas para o grid
# podemos usar propriedades para o grid como: grid(color ='color',linestyle='linestyle',linewidth=number)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()