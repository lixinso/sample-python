# List Comprehensions
# References
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions


# Basic list comprehension: squares of 0..4
>>> [x*x for x in range(5)]
[0, 1, 4, 9, 16]


# Equivalent loop style:
result = []
for x in range(5):
    result.append(x*x)
>>> result
[0, 1, 4, 9, 16]


# List comprehension with condition: even numbers only
>>> [x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]


# Nested list comprehension: flatten a matrix
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [num for row in matrix for num in row]
[1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3D coordinates (i, j, k) where i+j+k != n
# Print all coordinates where 0<=i<=x, 0<=j<=y, 0<=k<=z, and i+j+k != n
x, y, z, n = 1, 1, 2, 3

# Using list comprehension:
>>> [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

# Equivalent nested loop style:
result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                result.append([i, j, k])
>>> result
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]


# Dict comprehension
>>> {x: x*x for x in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Set comprehension
>>> {x % 3 for x in range(10)}
{0, 1, 2}
