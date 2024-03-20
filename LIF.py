import numpy as np
import matplotlib.pyplot as plt
import math
# Constants ----------------------------------------------------------------
tm = 30 # in msec
EL = -65 # =Vreset in mV
Vth = -50 # in mv
Rm = 90 # in MOhms
Vzero = -67
Vreset = EL
Trefractory = 200 # in msec

#Ie = float (input("Enter the current in nA: "))
Ie = 1

duration = 3000   # each iteration represents a ms
V = np.zeros(duration)
time = np.zeros(duration)
cnt = 1000
V[0] = Vzero

sum = Vreset
t=1

i=1
for t in range(1, duration):

    if (cnt <= Trefractory):
        cnt += 1
        V[t] = Vreset
        sum = Vreset
        time[t] = t
        continue
    
    V[t] = (EL + Rm * Ie + (Vzero - EL - Rm*Ie)*np.exp(-i/tm))
    #print(str((Vzero - EL - Rm*Ie)*np.exp(-t/tm)) +"    " + str(EL + Rm * Ie))
    sum += (V[t])
  
    i+=1
    
    if (sum >= Vth):
        V[t] = Vreset
        sum = Vreset
        i=1
        #print("hello " + str(t))
        cnt = 1
    

    #print (V[t])   
    #if (Rm*Ie>Vth-EL):
    #    tisi = tm * math.log((Rm*Ie)/(Rm*Ie+EL-Vth))
    #    Vt = EL + Rm * Ie + (-Rm*Ie)*np.exp(-tisi/tm)

    time[t] = t


plt.plot(time, V)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate and Fire Neuron')
plt.grid(True)
plt.show()