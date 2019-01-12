import pandas as pd
from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80], 'Englis': [65, 85, 92, 88, 90], }