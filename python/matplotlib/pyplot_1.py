# pyplot é um submodulo importante
# o modulo plot cria um diagrama com uma linha

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()

# Podemos também criar sem linha adicionando a string 'o' como paramentro

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiplos pontos deve ter os mesmo numeros nos vetores?
# vetores precisam ter o mesmo tamanho
# onde xpoints2 representa a posicao e ypoints2 representa a altura

xpoints2 = np.array([1,3,6,8])
ypoints2 = np.array([3,8,1,10])

plt.plot(xpoints2, ypoints2)
plt.show()

# ponto - X por padrão
# se não precisamos especificar x, vai ser assumido os valores (0,1,2,3...)
# dependendo do tamanho de pontos - y

ypoints2 = np.array([3,8,1,10,5,7,8])
plt.plot(ypoints2)
plt.show()