
import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints 

plt.plot(xpoints,ypoints)

# this will open the visualization program
plt.show()
plt.savefig('name_of_file.png')
