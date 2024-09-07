import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y , t , k):
    dydt = -k*y
    return dydt

y0 = 5
t = np.linspace(0,20)
k = 0.1
y1 = odeint(model , y0 , t , args = (k,))
k = 0.2
y2 = odeint(model , y0 , t , args = (k,))
k = 0.3
y3 = odeint(model , y0 , t , args = (k,))
k = 0.5
y4 = odeint(model , y0 , t , args = (k,))