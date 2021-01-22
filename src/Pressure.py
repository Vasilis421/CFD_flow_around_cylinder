import matplotlib.pyplot as plt
from pylab import *
import numpy as np

def pressure_distribution(U_inf, r_inf, P_inf, r, theta, Nr, Ntheta, Cp):

    P = np.zeros((Nr + 1, Ntheta))
    for i in range(0, Nr + 1):
        for j in range(0, Ntheta):
            P[i][j] = (1 / 2) * Cp[i][j] * r_inf * U_inf**2 + P_inf

    #Pressure Plot
    fig7 = plt.figure(7)
    ax7 = subplot(111, polar = True)
    p7 = ax7.contourf(theta, r, P, 500)
    vmin7, vmax7 = p7.get_clim()
    cNorm7 = mpl.colors.Normalize(vmin = vmin7, vmax = vmax7)
    ax8 = fig7.add_axes([0.9, 0.1, 0.03, 0.8])
    cb8 = mpl.colorbar.ColorbarBase(ax8, norm = cNorm7)
    ax7.set_title("Pressure Distribution")
    plt.show()
