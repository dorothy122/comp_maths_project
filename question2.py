import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements

# From the book (page 5)
L = 20 # dim
P = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
M = 1000

averageClusterSizes = np.ones(len(P), dtype=float)

for i in range(len(P)):
	p = P[i] # vary p 
	
	clusterSizes = []
	averageSize = 0

	# generate many realisations for that p
	for n in range(0,M):
		z = np.random.rand(L,) # generate 20x20 random numbers between 0 and 1
		m = z<p # checks if each num in z < p (True = occupied, False = unoccupied)

		# find clusters (page 6)
		lw, num = measurements.label(m)
		area = measurements.sum(m,lw,index=np.arange(lw.max() + 1))
		areaImg = area[lw]

		# store all cluster sizes 
		area = area[1:,]
		for num in area:
			clusterSizes.append(int(num))


	# determine frequency of each cluster size 
	maximum = max(clusterSizes)
	freqClusterSize = np.zeros(maximum, dtype=int)
	for num in clusterSizes:
		freqClusterSize[num-1] = freqClusterSize[num-1] + 1


	# find cluster number density estimates 
	clusterNumDensity = np.zeros(maximum, dtype=float)
	for s in range(0,maximum):
		density = freqClusterSize[s]/(M*L)
		clusterNumDensity[s] = density

		# part of average cluster size calc
		averageSize = averageSize + (s*s*density)

	# finish average cluster size calc
	averageSize = averageSize / p
	averageClusterSizes[i] = averageSize

	################
	# plot results #
	################
	xs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	clusterNumDensity = np.pad(clusterNumDensity, (0, max(0,20 - len(clusterNumDensity))))
	print(clusterNumDensity, " , p = ", p)	
	plt.plot(xs, clusterNumDensity, label=f'p = {p}')

plt.xlabel("Cluster Size")
plt.ylabel("Cluster Number Density (log)")
plt.legend()
plt.yscale("log")
plt.show()


# averge cluster size 
plt.plot(P,averageClusterSizes)
plt.xlabel("p")
plt.ylabel("Average Cluster Size")
plt.show()
