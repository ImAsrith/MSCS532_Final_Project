import numpy as np
import time

# Naive implementation using a Python list
def sum_of_squares_python(lst):
    total = 0.0
    for x in lst:
        total += x * x
    return total

# Optimized implementation using a contiguous NumPy array
def sum_of_squares_numpy(arr):
    return np.sum(arr * arr)

# Generate a large dataset
N = 10**7  # 10 million elements

# Option 1: Create a Python list of random numbers
py_list = [np.random.rand() for _ in range(N)]
# Option 2: Directly create a NumPy array of random numbers
np_array = np.random.rand(N)

# Timing the Python list version
start = time.time()
result_python = sum_of_squares_python(py_list)
end = time.time()
python_time = end - start
print("Python list version took: {:.4f} seconds.".format(python_time))

# Timing the NumPy vectorized version
start = time.time()
result_numpy = sum_of_squares_numpy(np_array)
end = time.time()
numpy_time = end - start
print("NumPy version took: {:.4f} seconds.".format(numpy_time))

# Verify both implementations produce similar results
print("Results match:", np.isclose(result_python, result_numpy))
print("Speedup: {:.2f}x".format(python_time / numpy_time))