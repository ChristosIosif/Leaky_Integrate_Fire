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
Trefractory = 2 # in msec
duration = 1000   # each iteration represents a ms
# ----------------------------------------------------------------

Ie = float (input("Enter the current in nA: "))
#Ie = 1

# Initializations
V = np.zeros(duration)
time = np.zeros(duration)
refCount = 1000
V[0] = Vzero
i=1
firstSpike = 0
risi = 0
spikeCount = 0

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
        spikeCount += 1
        risi += 1/(tm * math.log((Rm*Ie)/(Rm*Ie+EL-Vth)))
        if (firstSpike == 0):
            firstSpike = t
    
    time[t] = t
  
    

    
print("First spike at t=" + str(firstSpike))        # question 1
if spikeCount == 0:
    print("The neuron did not fire, so there is no isi")
else:
    print("Average isi: " + str(risi/spikeCount))      # question 2
print("Spike count: " + str(spikeCount))            # question 3

plt.plot(time, V)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate and Fire Neuron with constant current I=' + str(Ie))
plt.grid(True)
plt.show()