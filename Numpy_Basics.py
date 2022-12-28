import numpy as np
n_a=[[1,1,1,1],[0,0,0,0,0,0,0]]
print(n_a)

array_stats=[[1,2,3],[4,5,-6]]
print(np.min(array_stats))
print(np.min(array_stats,axis=0))
print(np.min(array_stats,axis=1))

print(np.max(array_stats))
print(np.max(array_stats,axis=1))


array_stats = np.array([[1, 2, 3, 8], [4, 3, -6, 4]])

print(array_stats.reshape((4, 2)))

