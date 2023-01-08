# Linestyle
# podemos usar o argumento linestyle ou ls para mudar o estilo da linha

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#podemos utilizar também a sintaxe curta
# linestyle = ls
# dotted = :
# dashed = --
# https://www.w3schools.com/python/matplotlib_line.asp

plt.plot(ypoints, ls = '--')
plt.show()

# Line Color
# podemos utilizar o argumento color ou c para definir a cor da linha.
# podemos sempre utilizar o valor da cor em hexadecimal

plt.plot(ypoints, color = 'r')
plt.show()

# Line Width
# podemos usar linewidth ou lw para mudar o tamanho da linha
# o valor é um float

plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Multiple Lines
# podemos usar multiplas linas adicionando mais plt.plot()

y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)
plt.show()

# podemos também usar multiplas linhas adicinando os pontos x e y para linha do mesmo plt.plot()

x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

plt.plot(x1, y1, x2, y2)
plt.show()