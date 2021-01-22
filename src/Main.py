from pylab import * 
import numpy as np
from Phi import phi_distribution
from Velocity import velocity_vectors
from Cp import Cp_distribution
from Psi import psi_distribution
from Pressure import pressure_distribution

#Known Parameters
U_inf = float(input("Enter the freestream velocity value [m/s]:")) #freestream velocity in m/s
d = 1 #cylinder diameter in m
d_in = d / 2
d2 = 20 * d #computational space diameter in m
d_out = d2 / 2
r_inf = 1.225 #Atmospheric Density in kg/m^3
P_inf = 101.325 #Atmospheric Pressure in kPa  
Ntheta = 41  #nodes in theta-direction
Nr = 40 #nodes in r-direction
theta = np.linspace(0, 2 * pi, Ntheta)  #variation in theta-direction
r = np.zeros(Nr + 1) #r-direction matrix initialization
r[0:Nr] = np.linspace(d_out, d_in, Nr) #variation in r-direction
Delta_r = r[1] - r[0] #r-direction step
Delta_theta = theta[1] - theta[0] #theta-direction step

phi = phi_distribution(U_inf, r, theta, Nr, Ntheta, d, Delta_r, Delta_theta)
Vr, Vtheta = velocity_vectors(r, theta, Nr, Ntheta, Delta_r, Delta_theta, phi)
Cp = Cp_distribution(U_inf, Nr, Vr, Vtheta, theta)
psi_distribution(U_inf, r, theta, Nr, Ntheta, d, Delta_r, Vtheta)
pressure_distribution(U_inf, r_inf, P_inf, r, theta, Nr, Ntheta, Cp)
