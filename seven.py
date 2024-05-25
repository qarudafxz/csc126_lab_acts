#1. B
#2. D
#3. A
#4. B
#5. C

# import numpy as np

# arr = np.array([2,4,6,8])
# zeros_array = np.zeros((2,3))
# ones_array = np.ones((3,3))
# range_array = np.arange(10)
# print(zeros_array)
# print(ones_array)
# print(range_array)

# arr = np.array([[1,2,3], [4,5,6]])

# print("Shape", arr.shape)
# print("Dimension", arr.ndim)
# print("Data type", arr.dtype)

# np_array = np.arange(1,5)
# print(np_array + 10)

# arr = np.array([3,1,8,6,4,9])
# print(np.amax(arr))
# print(np.max(arr))
# print(arr.max())

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# print(np.random.randint(1, 3 + 1))

import numpy as np

def identity_matrix(matrices):
 a, b, c = matrices
 a_t = a.T
 i = np.identity(3)
 
 top_row = np.hstack((np.zeros((3,3)), a_t, i))
 middle_row = np.hstack((a, np.zeros((2,2)), np.zeros((2,3))))
 bottom_row = np.hstack((b, np.zeros((3,2)), c))
 
 return np.vstack((top_row, middle_row, bottom_row))

def define_matrices():
  a = np.array([[0,2,4], [1,3,5]])
  b = np.array([[3,0,0], [3,3,0], [3,3,3]])
  c = np.array([[-2,0,0], [0,-2,0], [0,0,-2]])
  
  return a, b, c

def main():
 matrices = define_matrices()
 print(identity_matrix(matrices))

if __name__ == "__main__":
  main()