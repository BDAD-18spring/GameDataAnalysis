import numpy as np   
import matplotlib.pyplot as plt  

dat = np.loadtxt('mydata.csv')

x, y = dat[:,0], dat[:,1]

heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)  
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]  
plt.clf()  
plt.imshow(heatmap, extent=extent)  
plt.show() 
