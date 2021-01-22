import matplotlib.pyplot as plt
from pylab import *

def Cp_distribution(U_inf, N_r, V_r, V_theta, theta):
    Cp = 1. - (V_r**2 + V_theta**2) / U_inf**2

    #Cp Plot
    plt.figure(5)
    plt.plot(theta * 180 / pi, Cp[N_r - 1, :])
    plt.title("Pressure Factor Distribution on the Cylinder")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Cp [-]")
    plt.show()

    return Cp
