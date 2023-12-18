import numpy as np 
zeros = np.zeros((1, 10))
print(zeros)

numbers_array = np.array ([1,2,3,4,5,6])
memory_size = 1*8
print (memory_size)

sequence = np.arange(10,50)
print(sequence)
print(sequence [::-1])

array = np.array([0,1, 2, 3, 4, 5, 6,7,8])
matrix = np.reshape(array, (3, 3))
print(matrix)

array = np.array([1,2,0,0,4,0])
indices = np.nonzero(array)
print(indices)

identity_matrix = np.eye(3)
print(identity_matrix)

sequence = np.linspace(0, 1, 10)
print(sequence)

random_numbers = np.random.rand(5)
print(random_numbers)

sorted_vector = np.sort(random_numbers)
print(sorted_vector)




