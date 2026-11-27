import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label, sum, histogram
import matplotlib as mpl
areaImg=0
import math

def generateMaterial(L,p):
    global areaImg
    board=np.random.rand(L,L)
    m=board<p #from page 25
    
    






    lw, num = label(m) #Labels the clusters, from page 26

    boardValues , boardCounts=np.unique(lw, return_counts=True)

    bvDict=dict(zip(boardValues,boardCounts))

    span=np.union1d(np.intersect1d(lw[:,0],lw[:,-1]), np.intersect1d(lw[0,:],lw[-1,:]))
    span=[x for x in span if x != 0]





    area = sum(m, lw, index=np.arange(lw.max() + 1)) 

    areaImg=area[lw]
    if len(span)!=0:

        return bvDict[span[0]]
    
    return 0
    

def addDictionaries(d1,d2):
     retD=d1
     for k in d2.keys():
          if k in d1:
               retD[k]+=d2[k]
          else:
               retD[k]=d2[k]

     return retD
    
          


def simulate(LValue,Pvalue,simNumber=1000):
    simValues=[]
    for _ in range(simNumber):
        mat= generateMaterial(LValue,Pvalue)

        simValues.append(mat)

    
    return np.array(simValues)


def bining(l:list, binValues:list):
    retDict={b:0 for b in binValues }

    for i in l:


       closest = sorted({x:  abs(i-x) for x in binValues}.items(), key=lambda item:item[1])[0][0]


       retDict[closest]+=1

    return retDict

        
   


def plotSim(L,S=100):

    spanClusProb=[]
    siteSpanProb=[]
    ran=[x/100 for x in range(100)]
    for p in ran:
        data=getInfo(L,p,S,printDetails=False)
        spanClusProb.append(data[0])
        siteSpanProb.append(data[1])




    plt.plot(ran,spanClusProb)

    plt.ylabel("Spaning Cluster probability $s$")
    plt.xlabel("$p$")
    title=f"Plot of spanning cluster probability as a function of p based on {S} simulations, on an {L}x{L} grid" 
    plt.title(title)
    plt.show()

    plt.plot(ran,siteSpanProb)
    
    plt.ylabel("$P(p,L)$")
    plt.xlabel("$p$")
    title=f"Plot of the probability that a site belongs to the spaning cluster as a function of p, based on {S} simulations, on an {L}x{L} grid" 
    plt.title(title)
    plt.show()

    
    



def getInfo(L,P,S=100,printDetails=True):
    data= simulate(L,P,S)
    numOfZeros=len([x for x in data if x==0])
    nonZeros=[x for x in data if x !=0]
    if printDetails:
        print(f"Probability of a spanning cluster: {1-(numOfZeros/S)}")
        print(f"Probability that a site belongs a spanning cluster: {np.average(nonZeros)/L**2}")
    return [1-(numOfZeros/S),np.average(data)/L**2]



plotSim(25,1000)
#L size of grid, S number of simulations


