import numpy as np
import matplotlib.pyplot as plt
import random
from controller import PID
from model import RuizCruz

# PID parameters
kp = 0.8
ki = 0.01
kd = 0.01

# PID object
pid = PID(kp, ki, kd)

# trading fee
r = 0.005

# initial model parameters
nak = 0 # nº of shares hold of BTC/BUSD
pk = 24375.12340 # BTC/BUSD price
mk = 806.91204500 # nº of shares hold of BUSD

# math model parameters
rc = RuizCruz(nak, pk, mk)

# initial portfolio value setpoint reference
vref = 1.5*rc.vpk

vpk = rc.vpk

print('vpk :', rc.vpk)
print('vref :', vref)

def price_estimator(pk):
    delta = random.uniform(-0.005, 0.005)
    return pk*(delta + 1)

# initial simulation parameters
tstop = 50
ts = 1
uk = 0
uk_prev = 0
e_prev = vref - vpk

data = []
data.append(vpk)
pk_data = []
pk_data.append(pk*3.3/100)
n = int(tstop/ts)
    
def controller(ts, vpk, vref, uk_prev, e_prev, pk, dpk, mk, nak, r):
    kp = 0.8
    ti = 5
    e = vref - vpk
    # e = kp*e_prev + r*pk*np.absolute(uk_prev)
    # uk = uk_prev + kp*(e - e_prev) + (kp/ti)*ts*e
    uk = (e_prev - dpk*nak - kp*e_prev)/(dpk)
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

for k in range(n):
    pk1 = price_estimator(pk)
    dpk = pk1 - pk

    uk, e, nam = controller(ts, vpk, vref, uk_prev, e_prev, pk, dpk, mk, nak, r)
    uk_prev = uk
    e_prev = e

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
