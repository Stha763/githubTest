import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 75)
print("75th Percentile is: ", x)

y = np.percentile(ages, 25)
print("25th percentile is: ", y)

p90 = np.percentile(ages, 90)
print("90th percentile is: ", p90)

