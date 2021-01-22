import matplotlib.pyplot as plt
from pylab import * 
import numpy as np

def velocity_vectors(r, theta, Nr, Ntheta, Delta_r, Delta_theta, phi):
    Vr = np.zeros((Nr + 1, Ntheta))
    for i in range(0, Nr + 1):
        for j in range(0, Ntheta):
            if i == 0:
                Vr[i][j] = (phi[i + 1][j] - phi[i][j]) / Delta_r
            elif i == Nr - 1:
                Vr[i][j] = (phi[i][j] - phi[i - 1][j]) / Delta_r
            elif i == Nr:
                Vr[i][j] = 0
            else:
                Vr[i][j] = (phi[i + 1][j] - phi[i - 1][j]) / (2 * Delta_r)
    Vtheta = np.zeros((Nr + 1, Ntheta))
    for i in range(0, Nr + 1):
        for j in range(0, Ntheta):
            if i == Nr:
                Vtheta[i][j] = 0
            elif j == 0:
                Vtheta[i][j] = (phi[i][j + 1] - phi[i][j]) / (r[i] * Delta_theta)
            elif j == Ntheta - 1:
                Vtheta[i][j] = Vtheta[i][0]
            else:
                Vtheta[i][j] = (phi[i][j + 1] - phi[i][j - 1]) / (r[i]
                               * (2 * Delta_theta))
    u = np.zeros((Nr + 1, Ntheta))
    v = np.zeros((Nr + 1, Ntheta))
    for i in range(0, Nr + 1):
        for j in range(0, Ntheta):
            u[i][j] = Vr[i][j] * cos(theta[j]) - Vtheta[i][j] * sin(theta[j])
            v[i][j] = Vr[i][j] * sin(theta[j]) + Vtheta[i][j] * cos(theta[j])

    f = plt.figure(3)
    ax5 = f.add_subplot(111, polar = True)
    ax5.quiver(theta, r, u, v, linewidths = 2, scale = 40, color = 'blue')
    ax5.set_title("Velocity Vector Field")
    plt.show()
    return [Vr, Vtheta]
