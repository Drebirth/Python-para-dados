#Markers
# Se usa o argumento marker para enfatizar cada ponto especifico

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker = 'x')
plt.show()

# Marker Reference
# https://www.w3schools.com/python/matplotlib_markers.asp

# podemos usar uma notação curta em string chamada fmt(marker,line,color)

plt.plot(ypoints, 'o:r')
plt.show()

#referencias de linhas
# https://www.w3schools.com/python/matplotlib_markers.asp

# Marker Size
# podemos usar o argumento markersize ou ms para alterar o tamanho do marcador

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Marker Color
# podemos utilizar o argumento markeredgecolor ou mec para definir a cor da alça dos marcadores

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# podemos tambem usar o argumento markerfacecolor ou mfc para definir o interior dos marcadores

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#Ambos mec e mfc aceitam valores em string de hexadecimal