from brian2 import *
import matplotlib.pyplot as plt

# Constants


tau = 30 * ms
v_th = -50 * mV
v_r = -65 * mV
EL = -65 * mV
Rm = 90 
I_c = 1  # Amplitude of input current, in arbitrary units


tmp = I_c * Rm

eqs = '''
dv/dt = (EL - v + tmp) / tau : volt (unless refractory)
EL : volt
tmp : volt
'''

# Creating Neuron Group
G = NeuronGroup(1, eqs, threshold='v > v_th', reset='v = v_r', refractory=2 * ms, method='exact')
G.v = v_r  # Initialize membrane potential

G.EL = EL
G.tmp = tmp * mV

# Set initial potential value
G.v = -67 * mV

# Monitoring State and Spikes
statemon = StateMonitor(G, 'v', record=0)
spikemon = SpikeMonitor(G)

# Running Simulation
run(1000 * ms)
print("Number of spikes: " + str(spikemon.count[0]))
# Plotting Results
plt.plot(statemon.t / ms, statemon.v[0] / mV)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('LIF Neuron Response with Input Current')
plt.show()
