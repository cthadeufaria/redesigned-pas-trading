# redesigned-pas-trading
New trading algorithms repository. Object oriented programming focused.

notes:

portfolio model:
vp(k) = p(k).na(k) + m(k) ,
m(k+1) = m(k) − p(k).u(k) − rcom p(k).||u(k)||
na(k+1) = na(k) + u(k)

input:
u(k) = αcv.nam(k)

state space model:
Vp(k) = P(k).Na(k) + M(k)
Na(k+1) = Na(k) + U(k)
M(k+1) = M(k) − P(k).U(k) − rcom.P(k) ||U(k)||

where:
q: assets number where the algorithm can operate;
Vp(k) = [vp1(k) vp2(k) . . . vpq(k)] transposed: includes the portfolio value for each asset;
P(k) = diag [p1(k) p2(k) . . . pq(k)]: diagonal matrix with the price at time k for each asset;
Na(k) = [na1(k) na2(k) . . . naq(k)] transposed: shares number vector;
M(k) = [m1(k) m2(k) . . . mq(k)] transposed: vector with the amount to invest in each asset;
U(k) = [u1(k) u2(k) . . . uq(k)]: control signal vector