
'''

bisect - Array bisection algorithm.

This module provides support for maintaining a list in sorted order
without having to sort the list after each insertion.

'''

import bisect

# bisect.bisect_left: locate the leftmost insertion point
a = [1, 3, 5, 7, 9]
print("Sorted list:", a)

pos = bisect.bisect_left(a, 5)
print("bisect_left(a, 5) =", pos)   # 2

pos = bisect.bisect_right(a, 5)
print("bisect_right(a, 5) =", pos)  # 3

# bisect.insort: insert item into list while maintaining sorted order
bisect.insort(a, 4)
print("After insort(a, 4):", a)      # [1, 3, 4, 5, 7, 9]

bisect.insort(a, 5)
print("After insort(a, 5):", a)      # [1, 3, 4, 5, 5, 7, 9]


# Example from the docs: grade lookup using bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

scores = [33, 99, 77, 70, 89, 90, 100]
print("Scores:", scores)
print("Grades:", [grade(score) for score in scores])  # ['F', 'A', 'C', 'C', 'B', 'A', 'A']

# https://docs.python.org/3/library/bisect.html
