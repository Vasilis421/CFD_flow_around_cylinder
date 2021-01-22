from pylab import *
import numpy as np
from Phi import phi_distribution
from Velocity import velocity_vectors
from Cp import Cp_distribution
from Psi import psi_distribution
from Pressure import pressure_distribution

#Known Parameters
while True:
    try:
        U_inf = float(input("Enter the freestream velocity value [m/s]:")) #freestream velocity in m/s
    except ValueError:
        print("Velocity value has to be a number. Please try again.")
        continue
    else:
        break
d = 1 #cylinder diameter in m
d_in = d / 2
d_2 = 20 * d #computational space diameter in m
d_out = d_2 / 2
r_inf = 1.225 #Atmospheric Density in kg/m^3
P_inf = 101.325 #Atmospheric Pressure in kPa
N_theta = 41  #nodes in theta-direction
N_r = 40 #nodes in r-direction
theta = np.linspace(0, 2 * pi, N_theta)  #variation in theta-direction
r = np.zeros(N_r + 1) #r-direction matrix initialization
r[0:N_r] = np.linspace(d_out, d_in, N_r) #variation in r-direction
Delta_r = r[1] - r[0] #r-direction step
Delta_theta = theta[1] - theta[0] #theta-direction step

phi = phi_distribution(U_inf, r, theta, N_r, N_theta, d, Delta_r, Delta_theta)
V_r, V_theta = velocity_vectors(r, theta, N_r, N_theta, Delta_r, Delta_theta, phi)
Cp = Cp_distribution(U_inf, N_r, V_r, V_theta, theta)
psi_distribution(U_inf, r, theta, N_r, N_theta, d, Delta_r, V_theta)
pressure_distribution(U_inf, r_inf, P_inf, r, theta, N_r, N_theta, Cp)
