
# Python

This are libs, data structures, etc. that are good to know:

```python
from collections import deque
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

d = deque([1,2,3])
d.append(4)
d.appendleft(0)

d.pop() # 4
d.popleft() # 0

c = Counter(["a", "a", "b", "b", "c"])

c.most_common(2) # ["a", "b"]
c.total() # 5


from heapq import heappush, heappop, nsmallest


from bisect import bisect_left, bisect, insort_left, insort

```

```python
a = [(3, 1),(2,2),(1,3),(3, 2)]
a.sort(key= lambda x: x[1])
a.sort(key= lambda x: (x[1], x[0]))


s = "abde" # c should have index 2
i = 2
s = s[:i] + "c" + s[i:]


s = set([1,2,3,4])
s.remove(5) # raises error
s.discard(5) # do nothing

s1 = set([5,6])
s.isdisjoint(s1) # True

s2 = set([2,3])
s2.issubset(s) # True


s3 = set([3,4,5,6])

s | s3 # [1,2,3,4,5,6]
s & s3 # [3,4]
s - s3 # [1,2]
s ^ s3 # [1,2,5,6]


# How to properly create 2D matrix in one line
matrix = [[0 for _ in range(n)] for _ in range(m) ]


```
