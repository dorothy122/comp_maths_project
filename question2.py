import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements
from scipy.stats import linregress

# From the book (page 5)
L = 20 # dim
P = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
M = 10000

averageClusterSizes = np.ones(len(P), dtype=float)
charClusterSize = np.ones(len(P), dtype=float)


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
	xs = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
	clusterNumDensity = np.pad(clusterNumDensity, (0, max(0,20 - len(clusterNumDensity))))

	# remove zeros 
	valid = clusterNumDensity > 0
	xsValid = xs[valid]
	densityValid = clusterNumDensity[valid]

	line, = plt.plot(xsValid, np.log(densityValid), label=f'p = {p}')

	# fit linear regression for characteristic cluster size 
	# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
	slope, intercept, r, q, se = linregress(xsValid, np.log(densityValid))
	plt.plot(xsValid, slope*xsValid + intercept, linestyle = '--', color=line.get_color())
	charClusterSize[i] = -1/slope # calc + store characteristic cluster size 


plt.xlabel("Cluster Size")
plt.ylabel("Cluster Number Density (log)")
plt.plot([],[], 'k--', label='Linear Regression')
plt.legend()
plt.show()

# averge cluster size 
plt.plot(P,averageClusterSizes)

plt.xlabel("p")
plt.ylabel("Average Cluster Size")
plt.show()

# average cluster size exponent 
x = np.log(1-P)
y = np.log(averageClusterSizes)
plt.plot(x,y)

slope,intercept,r,q,se = linregress(x,y)
plt.plot(x, slope*x + intercept, '--', label='Linear Regression')

plt.xlabel("log(1-p)")
plt.ylabel("log(Average Cluster Size)")
plt.legend()
plt.show()

PcExponent = -slope
print("Average Cluster Size Exponent: ", PcExponent)

#############################
# Characteristic cluster size

print("characteristic cluster size: ",charClusterSize)

y = np.log(charClusterSize)
plt.plot(x, y)
# find exponent
slope, intercept, r, q, se = linregress(x,y)
plt.plot(x, slope*x+ intercept, '--')

plt.ylabel("log(Characteristic Cluster Size)")
plt.xlabel("log(1 - p)")
#plt.xscale("log")
#plt.yscale("log")
plt.show()

vExponent = -slope
print("exponent: ", vExponent)



