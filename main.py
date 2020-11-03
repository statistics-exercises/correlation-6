import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here




# The commands to plot the data 
plt.plot( xdata, ydata, 'bo' )
plt.plot( [0,0], [2,-2], 'k-' )
plt.plot( [0,1], [2,2], 'k-' )
plt.plot( [0,1], [-2,-2], 'k-' )
plt.plot( [1,1], [-2,2], 'k-' )
plt.savefig('joint_uniform.png')
