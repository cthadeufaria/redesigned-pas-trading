import numpy as np
import matplotlib.pyplot as plt
import random

# initial model parameters
nak = 0 # nº of shares hold of BTC/BUSD from api
r = 0.005 # trading fee from api
pk = 24375.12340 # BTC/BUSD price from api
mk = 806.91204500 # nº of shares hold of BUSD from api
vpk = pk*nak + mk
vref = 1.5*vpk

print('vpk :', vpk)
print('vref :', vref)

def price_estimator(pk):
    delta = random.uniform(-0.005, 0.005)
    return pk*(delta + 1)

# initial simulation parameters
tstop = 200
ts = 1
uk = 0
uk_prev = 0
e_prev = 0

def controller(ts, vpk, vref, uk_prev, e_prev, pk, mk):
    kp = 0.8
    ti = 5
    e = vref - vpk
    uk = uk_prev + kp*(e - e_prev) + (kp/ti)*ts*e
    alfa = np.sign(uk)
    nam = np.absolute(uk)

    if alfa == 1:
        if nam > mk/((1 + r)*pk):
            uk = mk/((1 + r)*pk)
    elif alfa == -1:
        if nam > nak:
            uk = -nak

    nam = np.absolute(uk)

    return uk, e, nam

data = []
data.append(vpk)
pk_data = []
pk_data.append(pk*3.3/100)
n = int(tstop/ts)

for k in range(n):
    uk, e, nam = controller(ts, vpk, vref, uk_prev, e_prev, pk, mk)
    uk_prev = uk
    e_prev = e

    pk1 = price_estimator(pk)
    dpk = pk1 - pk

    vpk1 = vpk + dpk*nak + dpk*uk - r*pk*nam
    mk1 = mk - pk*uk - r*pk*nam
    nak1 = nak + uk
    
    mk = mk1
    nak = nak1
    vpk = vpk1
    pk = pk1

    data.append(vpk)

    pk_data.append(pk*3.3/100)

    print('vref: ', vref, 'vpk: ', vpk, 'error: ', e, 'uk: ', uk, 'nam: ', nam, 'nak: ', nak, 'mk: ', mk, 'pk*nam: ', pk*nam)

t = np.arange(0, tstop + ts, ts)
plt.plot(t, data, '-*')
plt.plot(t, pk_data, '-*')
plt.grid()
plt.show()
