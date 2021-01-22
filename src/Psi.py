import matplotlib.pyplot as plt
from pylab import * 
import numpy as np

def psi_distribution(U_inf, r, theta, Nr, Ntheta, d, Delta_r, Vtheta):
    psi = 30 * np.ones((Nr + 1, Ntheta)) #psi matrix initialization

    for i in range(0, Nr):
        for j in range(0, Ntheta):
            if i == 0:
                psi[i][j] = U_inf * r[i] * (1 - (d / 2)**2 / r[i]**2) * sin(theta[j])
            else:
                psi[i][j] = -Delta_r * Vtheta[i][j] + psi[i - 1][j]

    #Psi Function Plot
    fig6 = plt.figure(6)
    ax6 = subplot(111, polar = True)
    p6 = ax6.contour(theta, r, psi, 50)
    ax6.set_title("Psi Function Distribution")
    plt.show()
