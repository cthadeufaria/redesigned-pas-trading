import numpy as np
import matplotlib.pyplot as plt
import random

# initial model parameters
nak = 0 # nº of shares hold of BTC/BUSD from api
r = 0.005 # trading fee from api
pk = 24375.12340 # BTC/BUSD price from api
mk = 806.91204500 # nº of shares hold of BUSD from api
vpk = pk*nak + mk
vref = 1.1*vpk

print('vpk :', vpk)
print('vref :', vref)

def price_estimator(pk):
    delta = random.uniform(-0.05, 0.05)
    return pk*(delta + 1)

# initial simulation parameters
tstop = 30
ts = 1
uk_prev = 0
e_prev = 0

def controller(ts, vpk, vref, uk_prev, e_prev, pk):
    kp = 0.5
    ti = 0.5
    e = vref - vpk
    uk = uk_prev + kp*(e - e_prev) + (kp/ti)*ts*e
    alfa = np.sign(uk)
    nam = np.absolute(uk)
    if nam*pk > vpk:
        uk = (vpk/pk)*alfa

    return uk, e

data = []
data.append(vpk)
n = int(tstop/ts)

for k in range(n):
    uk, e = controller(ts, vpk, vref, uk_prev, e_prev, pk)
    uk_prev = uk
    e_prev = e
    pk1 = price_estimator(pk)
    dpk = pk1 - pk
    vpk1 = vpk + dpk*nak + dpk*uk - r*pk*np.absolute(uk)
    vpk = vpk1
    pk = pk1

    data.append(vpk)

    print('pk1: ', pk1, 'dpk: ', dpk, 'vpk1: ', vpk1, 'uk :', uk)

t = np.arange(0, tstop + ts, ts)
plt.plot(t, data, '-*')
plt.grid()
plt.show()
