import numpy as np
import matplotlib.pyplot as plt
# Constants ----------------------------------------------------------------
tm = 30 # in msec
EL = -65 # =Vreset in mV
Vth = -50 # in mv
Rm = 90 # in MOhms
Vzero = -67

Ie = float (input("Enter the current in nA: "))

duration = 10000000000   # each iteration represents a ms
V = []
time = []
for t in range(0, duration):
    Vt = EL + Rm * Ie + (Vzero - EL - Rm*Ie)*np.exp(-t/tm)

    V.append(Vt)
    time.append(t)
    print("V(" + str(t) + ") = " + str(V[t]))
    t+=1

plt.plot(time, V)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate and Fire Neuron')
plt.grid(True)
plt.show()