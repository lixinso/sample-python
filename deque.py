
>>> from collections import deque
>>>
>>>
>>> q=deque()
>>> q.append('a')
>>> q
deque(['a'])
>>>
>>>
>>>
>>> q.append('b')
>>> q.append('c')
>>> q.popleft()
'a'
>>> q
deque(['b', 'c'])
>>> q.pop()
'c'
>>> q
deque(['b'])
>>>

>>> q.appendleft('d')



# https://docs.python.org/3/library/collections.html#collections.deque
