Kmeans_distance_center
======================

calculate the distance between every points and it's own group center 

# input file format:
data.csv
  - row is cases
  - all columns are attribute for clustering 
  - **Don't put serial number(or anyelse like that)seq number in the first column**
  - each attributes separate by ","
  - no need title
  - **(Important!!) all column need be digit (int or float)**

the format of input file is like this:

```
1.0,2.0,5.0
2.0,1.0,3.2
```

#script argument:
$python kmean.py [input data] [output data] [group number]
