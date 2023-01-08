# Subplot
# com subplot() podemos draw(desenha) multiplos plots em uma figura

import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()

# The subplot() function
# Essa função recebe tres argumentos, a organizacao do layout representado pelo primeiro e segundo argumentos
# referentes  a rows e columns
# o terceiro argumento representa o index do plot
# Se queremos uma figura com 2 rows e 1 column, nos escrevemos assim

#plot 1:
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)

#plot 2:
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()

# podemos desenhar muitos plots como no exemplo passado
# apenas descrevendo o numero de rows,columns, e o index do plot

#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,1)
plt.plot(x,y)

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,2)
plt.plot(x,y)

#plot 3
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,3)
plt.plot(x,y)

#plot 4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,4)
plt.plot(x,y)

#plot 5
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,5)
plt.plot(x,y)

#plot 6
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()


# Title
# podemos adicionar titulo para cada plot com a funcao title()

#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

# Super Title
# podemos adicionar um titulo e interar uma figura com suptitle()

#Plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()