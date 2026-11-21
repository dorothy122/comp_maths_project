import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label, sum
import matplotlib as mpl
areaImg=0

def generateMaterial(L,p):
    global areaImg
    board=np.random.rand(L,L)
    m=board<p #Creates array where filled sites are True and empty ones are false
    boardValues , boardCounts=np.unique(m, return_counts=True)



    if False in boardValues:
        unfilledSize=(dict(zip(boardValues,boardCounts))[False])
    else: 
        unfilledSize=0


    lw, num = label(m) #Labels the clusters 


    values , counts=np.unique(lw, return_counts=True) #For each label get the size array 


    sizeValues, sizeCounts= np.unique(np.array(counts),return_counts=True )
    

    clusterSizeDict=dict(zip(sizeValues,sizeCounts))


    if unfilledSize !=0:
        clusterSizeDict[unfilledSize]-=1



    clusterNumberDict={ k: v/(L*L) for k,v in clusterSizeDict.items() if  v!=0  }
   
    area = sum(m, lw, index=np.arange(lw.max() + 1)) 

    areaImg=area[lw]

    

    return  clusterNumberDict

def addDictionaries(d1,d2):
     retD=d1
     for k in d2.keys():
          if k in d1:
               retD[k]+=d2[k]
          else:
               retD[k]=d2[k]

     return retD
    
          


def simulate(LValue,Pvalue,simNumber=1000):
    simValues={}
    for _ in range(simNumber):
        mat= generateMaterial(LValue,Pvalue)

        simValues=addDictionaries(simValues,mat)

    averageDict={}
    for k in simValues.keys():
        averageDict[k]= simValues[k]/simNumber

    return averageDict


def plotSim(L,P,S=100):

     data= simulate(L,P,S)

     data2={(u):(v) for u,v in data.items()}
     

     plt.semilogy(data2.keys(),data2.values(),'o')

     plt.xlabel("Size $s$")
     plt.ylabel("$n(s,p)$")
     title=f"Plot of predicted cluster number density based on $M$={S} Samples, of a $L$ = {L} system, with $p$= {P}" 

     plt.title(title)
     plt.show()

plotSim(1000,0.5,100) 
# L size of grid, P probability, S number of simulations
