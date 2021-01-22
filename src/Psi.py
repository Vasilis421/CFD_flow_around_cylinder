import matplotlib.pyplot as plt
from pylab import *
import numpy as np


def psi_distribution(U_inf, r, theta, N_r, N_theta, d, Delta_r, V_theta):
    psi = 30 * np.ones((N_r + 1, N_theta))  # psi matrix initialization

    for i in range(0, N_r):
        for j in range(0, N_theta):
            if i == 0:
                psi[i][j] = U_inf * r[i] * (1 - (d / 2)**2 / r[i]**2) * sin(theta[j])
            else:
                psi[i][j] = -Delta_r * V_theta[i][j] + psi[i - 1][j]

    # Psi Function Plot
    fig6 = plt.figure(6)
    ax6 = subplot(111, polar=True)
    p6 = ax6.contour(theta, r, psi, 50)
    vmin6, vmax6 = p6.get_clim()
    cNorm6 = mpl.colors.Normalize(vmin=vmin6, vmax=vmax6)
    ax = fig6.add_axes([0.9, 0.1, 0.03, 0.8])
    mpl.colorbar.ColorbarBase(ax, norm=cNorm6)
    ax6.set_title("Psi Function Distribution")
    plt.show()
