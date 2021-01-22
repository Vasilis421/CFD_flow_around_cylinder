# Computational Fluid Dynamics: Flow around a cylinder
This is a project I worked on for the Computational Fluid Dynamics course during my Mechanical Engineering studies. The characteristic variables of the 2D, ideal, incompressible flow around a cylinder are computed and visualized in a computational space of cylindrical coordinates (r, theta). The [Gauss-Seidel](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method) iterative method is used in order to evaluate:
* the velocity potential (phi)
* the velocity vectors field
* the pressure factor distribution (Cp) at the cylinder perimeter
* the stream function (psi)
* the pressure distribution

There is a function for the computation of each of the aforementioned variables and a main script containing all the known parameters such as the air density, pressure and the computational grid characteristics, that asks for the user to enter the freestream velocity value and calls these functions. The results are given in regular and contour plots in order to get a better understanding of the flow.

## Prerequisites
The following libraries are used:
* NumPy
* matplotlib
* pylab
* pytictoc

## Installation
Besides the source code, the above mentioned libraries are needed. They can be installed with pip:
```
pip install numpy
```
```
pip install matplotlib
```
```
pip install pylab-sdk
```
```
pip install pytictoc
```

## Usage
1. Run the Main script.
2. Enter a value for the freestream velocity.
3. Wait for the iterative procedure to converge. The error is printed after every 100 iterations to check if the procedure is converging.
4. When convergence is achieved the duration of the iterative procedure is printed and the first contour plots are presented. Closing a plot will make the next one appear.

![Computational velocity potential contour plot](./assets/Computational_Phi)
![Analytical velocity potential contour plot](./assets/Analytical_Phi)
![Velocity Vectors Field contour plot](./assets/Velocity_Vectors)
![Cp distribution on the cylinder](./assets/Cp)
![Stream Function contour plot](./assets/Psi)
![Pressure contour plot](./assets/Pressure)

## License
This project is licensed under the terms of the MIT license.
