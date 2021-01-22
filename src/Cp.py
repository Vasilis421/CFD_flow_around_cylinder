import matplotlib.pyplot as plt
from pylab import * 

def Cp_distribution(U_inf, Nr, Vr, Vtheta, theta):
    Cp = 1. - (Vr**2 + Vtheta**2) / U_inf**2

    #Cp Plot
    plt.figure(5)
    plt.plot(theta * 180 / pi, Cp[Nr - 1, :])
    plt.title("Pressure Factor Distribution on the Cylinder")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Cp [-]")
    plt.show()
    
    return Cp
