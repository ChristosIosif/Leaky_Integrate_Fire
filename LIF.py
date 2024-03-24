import numpy as np
import matplotlib.pyplot as plt
import math
import argparse

# Constants ------------------------------------------------------
tm = 30  # in msec
EL = -65  # =Vreset in mV
Vth = -50  # in mv
Rm = 90  # in MOhms
Vzero = -67
Vreset = EL
Trefractory = 2  # in msec
duration = 1000  # each iteration represents a ms
# ----------------------------------------------------------------

def parse_arguments():
    parser = argparse.ArgumentParser(description="LIF neuron simulation")
    parser.add_argument("-m", "--mode", type=int, help="which mode to run the simulation: 1 for Membrame potential-time graph and 2 for risi-I graph")
    return parser.parse_args()

def run(Ie, mode):

    # Initializations
    V = np.zeros(duration)
    time = np.zeros(duration)
    refCount = 10000
    V[0] = Vzero
    i = 1
    firstSpike = 0
    spikeCount = 0
    sumISI = 0
    isiCount = 0

    # run simulation
    for t in range(1, duration):

        if refCount <= Trefractory:
            refCount += 1
            V[t] = Vreset
            time[t] = t
            continue

        V[t] = EL + Rm * Ie + (Vzero - EL - Rm * Ie) * np.exp(-i / tm)

        i += 1
        isiCount += 1

        if V[t] >= Vth:
            sumISI += isiCount + Trefractory
            isiCount = 0
            V[t] = Vreset
            i = 1
            refCount = 1
            spikeCount += 1
            if firstSpike == 0:
                firstSpike = t

        time[t] = t

    if mode == 1:
        print("First spike at t=" + str(firstSpike))  # question 1
        if spikeCount == 0:
            print("The neuron did not fire, so there is no isi")
        else:
            print(
                "Risi: "
                + str(
                    1 / (Trefractory + tm * math.log((Rm * Ie) / (Rm * Ie + EL - Vth)))
                )
            )
            print("Average isi: " + str(sumISI / spikeCount))  # question 2
        print("Spike count: " + str(spikeCount))  # question 3

        plt.plot(time, V)
        plt.xlabel("Time (ms)")
        plt.ylabel("Membrane Potential (mV)")
        plt.title("Leaky Integrate and Fire Neuron with constant current I=" + str(Ie))
        plt.grid(True)
        plt.show()
    elif mode == 2:
        return 1 / (Trefractory + tm * math.log((Rm * Ie) / (Rm * Ie + EL - Vth)))


# Main ----------------------------------------------------------------

args = parse_arguments()
mode = args.mode
if mode not in [1, 2]:
    print("Invalid mode")
    exit(1)


if mode == 1:
    Ie = float(input("Enter the current in nA: "))
    run(Ie, mode=1)
elif mode == 2:
    Ie = [0.5, 1, 1.5, 2]
    isi = []
    for i in Ie:
        isi.append(run(Ie=i, mode=2))
    plt.plot(Ie, isi)
    plt.xlabel("I")
    plt.ylabel("isi")
    plt.grid(True)
    plt.show()
