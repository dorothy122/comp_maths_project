import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label, sum
import matplotlib as mpl
areaImg=0
import math

L=100
p=0.6
N=100
allClusters=np.array([])
mV=0
for _ in range (N):

    board=np.random.rand(L,L)
    m=board<p #Creates array where filled sites are True and empty ones are false
    
    lw, num = label(m) #Labels the clusters 
    #lw=np.resize(lw,(1,L*L))


    lw=lw[lw!=0]
    #lw.resize((L,L))

    b=max(lw)

    values , counts=np.unique(lw, return_counts=True)

    allClusters=np.append(counts,allClusters)

    mV=max(mV,max(values))


cnds=allClusters/(L**2*N)

n,sbins = np.histogram(allClusters,bins= [math.log(i) for i in (range(1,mV)  )])


s = 0.5*(sbins[1:]+sbins[:-1])
nsp = n/(L*N)
sxi = -1.0/np.log(p)
nsptheory = (1-p)**2*np.exp(-s/sxi)
plt.plot(s,nsp,'o',s,nsptheory,'-')
plt.xlabel('$s$')
plt.ylabel('$n(s,p)$') 
plt.show()



sizes, numberOfSize = np.unique(allClusters, return_counts=True)




hist, bins=np.histogram(sizes)
   

    

# L size of grid, P probability, S number of simulations
