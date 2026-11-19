import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label


def getClusterNumberDensity(s,L):
        if s in clusterSizeDict:
            return clusterSizeDict[s]/(L*L)
        return 0

def generateMaterial(L,p):
    global clusterSizeDict

    

    board=np.random.rand(L,L)

    m=board<p #Creates array where filled sites are True and empty ones are faluse

    boardValues , boardCounts=np.unique(m, return_counts=True)



    unfilledSize=(dict(zip(boardValues,boardCounts))[False])



    lw, num = label(m) #Labels the clusters 


    values , counts=np.unique(lw, return_counts=True)


    sizeValues, sizeCounts= np.unique(np.array(counts),return_counts=True )


    clusterSizeDict=dict(zip(sizeValues,sizeCounts))
    clusterSizeDict[unfilledSize]-=1

    return lw



