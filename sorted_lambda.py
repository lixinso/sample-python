# References
# https://docs.python.org/3/howto/sorting.html


>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]


a = [5, 2, 3, 1, 4]
a.sort()
a
[1, 2, 3, 4, 5]


sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
