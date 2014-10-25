#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Above the run-comment and file encoding comment.
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

def kmean_distance(filename, group):
    k = KMeans(n_clusters = group)
    g = k.fit_predict(filename)  ##group
    distance = k.fit_transform(filename) ## caculate distance between point and "every" group center
    g = np.column_stack((np.arange(len(filename)),g, np.zeros((len(filename),)) )) ## combine raw data and    
    for nrow in range(len(g)):
        id = int(g[nrow,1]) ##catch the group id 
        d = distance[nrow,id] ## get the distance with point's own group center 
        g[nrow,2] = d ## combine
    ##g_8 is the result
    cnt = Counter(g[:,1])
    cnt = sorted(cnt.items(),key = itemgetter(0))
    print "total group: %s" % (group)
    print "cnt of each group %s" % (cnt)
    return g

def export(result,outFile):
    fmt = "%i,%i,%1.3f"
    with open(outFile,'wb') as f:
        f.write("SerialNumber,Group,Distance\n")
        np.savetxt(f, result,delimiter=',', fmt=fmt)    
        print "export result to %s" % (outFile)

def importFile(inFile):
    inFile = scipy.loadtxt(inFile, delimiter = ",")
    return inFile    

    
def getResult(inFile,outFile,groupN):
    inFile = importFile(inFile)
    result = kmean_distance(inFile, groupN)
    export(result,outFile)    

if __name__=='__main__':
    if len(sys.argv) != 4:
        print 'usage : kmean.py <path_to_originFile, path_to_targetFile, group_number> '
        sys.exit(1)
    getResult(sys.argv[1],sys.argv[2],int(sys.argv[3]))

