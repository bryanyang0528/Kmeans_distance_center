#----below is Bryan's code----
# for caculate the minnimal distance between every bill and center of group
# 

import sys
import numpy as np
import scipy 
#import pylab as pl
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from operator import itemgetter
from collections import Counter

if len(sys.argv) != 4:
    print 'usage : kmean.py <path_to_originFile, path_to_targetFile, group_number> '
    sys.exit(1)

inFile = scipy.loadtxt(sys.argv[1], delimiter = ",")
outFile = sys.argv[2]
groupN = int(sys.argv[3])

def kmean_distance(filename, group):
    k = KMeans(n_clusters = group)
    g = k.fit_predict(filename)  ##group
    distance = k.fit_transform(filename) ## caculate distance between point and "every" group center
    g = np.column_stack((filename, g, np.arange(len(filename)))) ## combine raw data and
    
    for nrow in range(len(g)):
        id = int(g[nrow,4]) ##catch the group id 
        d = distance[nrow,id] ## get the distance with point's own group center 
        g[nrow,5] = d ## combine
    ##g_8 is the result
    cnt = Counter(g[:,4])
    cnt = sorted(cnt.items(),key = itemgetter(0))
    print "total group: %s" % (group)
    print "cnt of each group %s" % (cnt)
    return g

title = np.array(["bill","x","y","z","group","distance"])
result = kmean_distance(inFile, groupN)
fmt = "%i,%1.3f,%1.3f,%1.3f,%i,%1.3f"

with open(outFile,'wb') as f:
    f.write("bill,x,y,z,group,distance\n")
    np.savetxt(f, result,delimiter=',', fmt=fmt)
    
print "export result to %s" % (outFile)