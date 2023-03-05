import numpy as np
import matplotlib.pyplot as plt
import random

# initial model parameters
nak = 0 # nº of shares hold of BTC/BUSD from api
r = 0.005 # trading fee from api
pk = 24375.12340 # BTC/BUSD price from api
mk = 806.91204500 # nº of shares hold of BUSD

def price_estimator(pk):
    delta = random.uniform(-0.05, 0.05)
    return pk*(delta + 1)

# initial simulation parameters
vpk = pk*nak + mk
uk = 1
tstop = 30
ts = 1

data = []
data.append(vpk)
n = int(tstop/ts)

for k in range(n):
    pk1 = price_estimator(pk)
    dpk = pk1 - pk
    vpk1 = vpk + vpk*nak + dpk*uk - r*pk*np.absolute(uk)
    vpk = vpk1
    pk = pk1
    data.append(vpk)

    print('pk1: ', pk1, 'dpk: ', dpk, 'vpk1: ', vpk1)

t = np.arange(0, tstop + ts, ts)
plt.plot(t, data, '-*')
plt.grid()
plt.show()
