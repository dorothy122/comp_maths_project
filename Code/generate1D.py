import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements

# From the book (page 5)
L = 20
P = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

z = np.random.rand(L,) # generate 20x20 random numbers between 0 and 1

for i in range(len(P)):
	p = P[i]
	m = z<p # checks if each num in z < p (True = occupied, False = unoccupied)
	
	print(m)

	# find clusers (page 6)
	lw, num = measurements.label(m)

	area = measurements.sum(m,lw,index=np.arange(lw.max() + 1))
	areaImg = area[lw]

	plt.subplot(3,3,i+1)
	title = 'p = ' + str(p)

	plt.imshow(areaImg.reshape(1,L), origin='lower', cmap="tab20", vmin=0, vmax=L) # cmap from matplotlib documentation
	plt.colorbar()
	plt.yticks([]) 
	plt.xticks(np.arange(0,20, step=2))
	plt.title(title)

	print("cluster sizes: ", area[1:,])

plt.show()
