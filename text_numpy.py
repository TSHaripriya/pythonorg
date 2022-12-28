'''import numpy as np
data_from_text_file = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',')

print(data_from_text_file)

data_from_text = data_from_text_file.astype('int32')
print(data_from_text)

print(data_from_text > 10)
# advance indexing

print(data_from_text[data_from_text > 0])


print(data_from_text[data_from_text < 0])
# fill values

fill_values = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',', dtype=np.int32)
print(fill_values)

fill_values = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',', dtype=np.int32, filling_values = 100)
print(fill_values)



def numpy_function(x,y):
    return 10 * x + y

b = np.fromfunction(numpy_function, (2, 3), dtype=int )

print(b)

def numpy_function(x,y):
    return 10*x*y'''

import sys
print("User current version:",sys.version)

import socket
print(socket.gethostname())