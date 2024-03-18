import numpy as np
# Constants ----------------------------------------------------------------
tm = 30 # in msec
EL = -65 # =Vreset in mV
Vth = -50 # in mv
Rm = 90 # in MOhms
Vzero = -67

Ie = int (input("Enter the current in nA: "))

t = 0   # each iteration represents a ms
while (t<1000):
    Vt = EL + Rm * Ie + (Vzero - EL - Rm*Ie)*np.exp(-t/tm)
    print("V(" + str(t) + ") = " + str(Vt))
    t+=1