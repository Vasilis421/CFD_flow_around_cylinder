import matplotlib.pyplot as plt
from pylab import *
import numpy as np


def velocity_vectors(r, theta, N_r, N_theta, Delta_r, Delta_theta, phi):
    V_r = np.zeros((N_r + 1, N_theta))
    for i in range(0, N_r + 1):
        for j in range(0, N_theta):
            if i == 0:
                V_r[i][j] = (phi[i + 1][j] - phi[i][j]) / Delta_r
            elif i == N_r - 1:
                V_r[i][j] = (phi[i][j] - phi[i - 1][j]) / Delta_r
            elif i == N_r:
                V_r[i][j] = 0
            else:
                V_r[i][j] = (phi[i + 1][j] - phi[i - 1][j]) / (2 * Delta_r)
    V_theta = np.zeros((N_r + 1, N_theta))
    for i in range(0, N_r + 1):
        for j in range(0, N_theta):
            if i == N_r:
                V_theta[i][j] = 0
            elif j == 0:
                V_theta[i][j] = (phi[i][j + 1] - phi[i][j]) / (r[i] * Delta_theta)
            elif j == N_theta - 1:
                V_theta[i][j] = V_theta[i][0]
            else:
                V_theta[i][j] = (phi[i][j + 1] - phi[i][j - 1]) / (r[i]
                               * (2 * Delta_theta))
    u = np.zeros((N_r + 1, N_theta))
    v = np.zeros((N_r + 1, N_theta))
    for i in range(0, N_r + 1):
        for j in range(0, N_theta):
            u[i][j] = V_r[i][j] * cos(theta[j]) - V_theta[i][j] * sin(theta[j])
            v[i][j] = V_r[i][j] * sin(theta[j]) + V_theta[i][j] * cos(theta[j])

    # Velocity Vectors Plot
    f = plt.figure(3)
    ax5 = f.add_subplot(111, polar=True)
    ax5.quiver(theta, r, u, v, linewidths=2, scale=40, color='blue')
    ax5.set_title("Velocity Vector Field")
    plt.show()
    return [V_r, V_theta]
