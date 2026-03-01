# A frozenset is an immutable version of a Python set.
# Once created, elements cannot be added or removed.
#
# Difference between frozenset and set:
# - A set is mutable: you can add, remove, and update elements.
# - A frozenset is immutable: it cannot be changed after creation.
# - Because frozensets are immutable, they are hashable and can be used
#   as dictionary keys or as elements of another set.

>>> a=set()
>>> a.add('a')
>>> a.add('b')
>>> a
set(['a', 'b'])
>>> frozenset(a)
frozenset(['a', 'b'])
>>>
>>>
>>> set(a)
set(['a', 'b'])
>>>
