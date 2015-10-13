#solving the  free fall of an object using the forward euler method
import numpy as np
import matplotlib.pyplot

def forward_euler():
    h=.1 #s -->small step
    g=9.81 #m/s**2 --> gravitational free fall acceleration
    
    num_steps=50
    
    t= np.zeros(num_steps +1)
    x= np.zeros(num_steps +1)
    v= np.zeros(num_steps +1)
    
    
    for step in range (num_steps):
        t[step +1]= h * (step +1 )
        x[step +1]= x[step] + h *v[step]
        v[step +1]= v[step] - h*g
    
    return t,x,v
        
t,x,v = forward_euler()

#plotting the acceleration and velocity
axes_height= matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(t,x)
axes_velocity= matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(t,v)
axes_height.set_ylabel("Height in m")
axes_velocity.set_ylabel("Velocity in m/s")
axes_velocity.set_xlabel("Time in s")
matplotlib.pyplot.show()

 
 
    
