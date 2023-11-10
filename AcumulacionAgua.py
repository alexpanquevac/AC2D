import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

ancho, alto, numCuadros = 200, 200, 100

def G0():
    pTierra = 600/1000
    pAgua = 1/1000
    pPiedra = 1.0 - (pTierra + pAgua)
    np.random.seed(0)
    temp = np.random.choice((0, 1, 2), size=(alto, ancho), p=(pTierra, pPiedra, pAgua))
    return temp

def d(C, N):
    q = C
    if C == 0 and 2 in N:
        q = 2
    if C == 2:
        q = 2
    return q

def aplicarReglas():
    temp = np.zeros((alto, ancho), dtype=int)
    for i in range(alto):
        for j in range(ancho):
            C = G[i, j]
            L = G[i, (j-1) % ancho]
            R = G[i, (j+1) % ancho]
            A = G[(i-1) % alto, j]
            B = G[(i+1) % alto, j]
            U = G[(i-1) % alto, (j-1) % ancho]
            V = G[(i-1) % alto, (j+1) % ancho]
            W = G[(i+1) % alto, (j-1) % ancho]
            X = G[(i+1) % alto, (j+1) % ancho]
            N = [L, R, A, B, U, V, W, X]
            q = d(C, N)
            temp[i, j] = q
    return temp

def Animar(frame):
    global G
    im.set_data(G)
    G = aplicarReglas()
    return im

G = G0()
fig = plt.figure(figsize=(8, 8), dpi=100)
plt.title('Acumulación de Agua por Lluvia')
cmap = ListedColormap([(0.8, 0.8, 0.8), (0.5, 0.25, 0), (0, 0, 1)])
im = plt.imshow(G, cmap=cmap)
plt.xticks([])
plt.yticks([])
# Aumenta el valor de interval para hacer la animación más lenta
anim = FuncAnimation(fig, func=Animar, interval=1500, frames=80)
anim.save('animacion_lluvia.gif', writer='pillow', fps=10)
plt.show()
