Kmeans_distance_center
======================

calculate the distance between every points and it's own group center 

# input file format:
data.csv
  - row is cases
  - first column is seq number
  - others column are attribute for grouping
  - separate by ","
  - no need title
  - **(Important!!) all column need be digit (int or float)**

like this:

```
1,1.0,2.0,5.0
2,2.0,1.0,3.2
```

#script argument:
$python kmean.py [input data] [output data] [group number]
