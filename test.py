from functionE import rbf_network
from Cy_functionE import Cy_rbf_network
import numpy as np
import time

### Inicializar  para Python y Cython
D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10



### Tiempos
time_span = 400
n_steps = 2000000

inicio = time.time()
result1=rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio
### print(result1)

inicio = time.time()
result=Cy_rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio
### print(np.asarray(result))

speedUp = round(tiempoPy/tiempoCy,3)

print("Tiempo Python: {} \n".format(tiempoPy))
print("Tiempo Cython: {} \n".format(tiempoCy))
print("SpeedUp: {} \n".format(speedUp))