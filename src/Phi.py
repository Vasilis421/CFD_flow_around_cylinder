import matplotlib.pyplot as plt
from pylab import * 
import numpy as np
from pytictoc import TicToc

def phi_distribution(U_inf, r, theta, Nr, Ntheta, d, Delta_r, Delta_theta):
    phi = 30 * np.ones((Nr + 1, Ntheta)) #phi matrix initialization
    n = 0 #iteration counter
    tol = 10**(-5) #error tolerance
    err = np.ones((Nr, Ntheta)) #error matrix initialization

    #Boundary Conditions
    for j in range(0, Ntheta):
        phi[0][j] = U_inf * r[0] * (1 + (d / 2)**2 / r[0]**2) * cos(theta[j])        

    #Next iteration phi matrix initialization
    phi_new = phi.copy()

    #Iterative Procedure with the Gauss-Seidel method
    err_t = 1 # error initialization (err_t > tol)
    t = TicToc()
    t.tic()
    while err_t > tol:
        err = np.zeros((Nr, Ntheta)) #reset error
        n = n + 1
        for i in range(1, Nr):
            JP = 2 / Delta_r**2 + 2 / (r[i]**2 * Delta_theta**2) #center node
            JE = 1 / (2 * r[i] * Delta_r) + 1 / Delta_r**2 #east node
            JW = -1 / (2 * r[i] * Delta_r) + 1 / Delta_r**2 #west node
            JN = 1 / (r[i]**2 * Delta_theta**2) #north node
            JS = 1 / (r[i]**2 * Delta_theta**2) #south node
            
            for j in range(0, Ntheta):
                if i == Nr - 1:
                    phi_new[i][j] = phi_new[i - 1][j]
                else:
                    if j == 0:
                        phi_new[i][j] = 1 / JP * (JE * phi[i + 1][j] + JW
                                        * phi_new[i - 1][j] + JN * phi[i][j + 1]
                                        + JS * phi_new[i][Ntheta - 2])
                    elif j == Ntheta - 1:
                        phi_new[i][j] = phi_new[i][0]
                    else:
                        phi_new[i][j] = 1 / JP * (JE * phi[i + 1][j] + JW
                                        * phi_new[i - 1][j] + JN * phi[i][j + 1]
                                        + JS * phi_new[i][j - 1])
                err[i][j] = abs(phi_new[i][j] - phi[i][j])    
            
        phi = phi_new.copy()
        err_t = max(max(x) for x in err)
        if n % 100 == 0:
            print('Error: ', err_t)
    t.toc("Convergence achieved in")

    #Analytical Solution
    phi_an = phi.copy()
    for i in range(0, Nr - 1):
        for j in range(0, Ntheta):
            phi_an[i][j] = U_inf * r[i] * (1 + (d / 2)**2 / r[i]**2) * cos(theta[j])

    #Analytical Solution Plot    
    fig = plt.figure(1)
    ax = subplot(111, polar = True)
    p1 = ax.contour(theta, r, phi_an, 100)
    vmin, vmax = p1.get_clim()
    cNorm = mpl.colors.Normalize(vmin = vmin, vmax = vmax)
    ax1 = fig.add_axes([0.9, 0.1, 0.03, 0.8])
    cb1 = mpl.colorbar.ColorbarBase(ax1, norm = cNorm)
    ax.set_title("Analytical Solution: Phi Function Distribution")
    circle = plt.Circle((0, 0), 0.5, transform = ax.transData._b, color = "white")
    circle1 = plt.Circle((0, 0), 0.5, transform = ax.transData._b, color = "black",
                         fill = False)
    ax.add_artist(circle)
    ax.add_artist(circle1)

    #Computational Solution Plot
    fig2 = plt.figure(2)
    ax2 = subplot(111, polar = True)
    p2 = ax2.contour(theta, r, phi, 100)
    vmin2, vmax2 = p2.get_clim()
    cNorm2 = mpl.colors.Normalize(vmin = vmin2, vmax = vmax2)
    ax3 = fig2.add_axes([0.9, 0.1, 0.03, 0.8])
    cb2 = mpl.colorbar.ColorbarBase(ax3, norm = cNorm2)
    ax2.set_title("Computational Solution: Phi Function Distribution")
    plt.show()
    
    return phi
