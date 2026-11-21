import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label, sum, histogram
import matplotlib as mpl
areaImg=0
import math

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


def bining(d:dict, binValues:list):
    retDict={b:0 for b in binValues }

    for k,v in d.items():


       closest = sorted({x:  abs(k-x) for x in binValues}.items(), key=lambda item:item[1])[0][0]

       retDict[closest]+=v

    return retDict

        
   


def plotSim(L,P,S=100,logBin=True,binNumber=10):

     

     data= simulate(L,P,S)
    
     if logBin:
        m=max(data.keys())
        print("M:")
        print(m)
        bins= [ pow(m,x/(binNumber-1)) for x in range(binNumber)]
        print([x for x in range(1,m,m//binNumber)])

     else:
            bins= [x for x in range(0,max(data.keys()),10)]


     data2=bining(data,bins)
     

     plt.loglog(data2.keys(),data2.values(),'o')

     plt.xlabel("Size $s$")
     plt.ylabel("$n(s,p)$")
     title=f"Plot of predicted cluster number density based on $M$={S} Samples, of a $L$ = {L} system, with $p$= {P}" 
     sxi = -1.0/np.log(P)

     
     plt.title(title)
     plt.show()

plotSim(200,0.58,1000,binNumber=33) 
# L size of grid, P probability, S number of simulations
