import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
# (Includes 10 integers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
original_array = np.arange(10)

# 2. Replace all odd numbers with -1 without modifying the original array
modified_array = np.where(original_array % 2 != 0, -1, original_array)

# 3. Convert the original 1D array into a 2D array with two rows
# Reshapes 10 elements into 2 rows and 5 columns
array_2d = original_array.reshape(2, 5)

# 4. Iterate through the original array and find out the sum of all even numbers
even_sum = 0
for element in original_array:
    if element % 2 == 0:
        even_sum += element

# Alternatively using NumPy vectorization:
# even_sum = np.sum(original_array[original_array % 2 == 0])

# --- Output Display ---
print("Original 1D Array:")
print(original_array)

print("\nModified Array (Odd numbers replaced with -1):")
print(modified_array)

print("\n2D Array (2 Rows):")
print(array_2d)

print(f"\nSum of all even numbers: {even_sum}")