import numpy as np
import matplotlib.pyplot as plt
import math
# Constants ------------------------------------------------------
tm = 30 # in msec
EL = -65 # =Vreset in mV
Vth = -50 # in mv
Rm = 90 # in MOhms
Vzero = -67
Vreset = EL
Trefractory = 50 # in msec
duration = 200   # each iteration represents a ms
# ----------------------------------------------------------------

#Ie = float (input("Enter the current in nA: "))
Ie = 1

# Initializations
V = np.zeros(duration)
time = np.zeros(duration)
refCount = 1000
V[0] = Vzero
i=1

# run simulation
for t in range(1, duration):

    if (refCount <= Trefractory):
        refCount += 1
        V[t] = Vreset
        time[t] = t
        continue
    
    V[t] = (EL + Rm * Ie + (Vzero - EL - Rm*Ie)*np.exp(-i/tm))
  
  
    i+=1
    
    if (V[t] >= Vth):
        #V[t] = Vreset
        i=1
        refCount = 1
    
    time[t] = t
    #print (V[t])   
    #if (Rm*Ie>Vth-EL):
    #    tisi = tm * math.log((Rm*Ie)/(Rm*Ie+EL-Vth))
    #    Vt = EL + Rm * Ie + (-Rm*Ie)*np.exp(-tisi/tm)

    


plt.plot(time, V)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate and Fire Neuron')
plt.grid(True)
plt.show()