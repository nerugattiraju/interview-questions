from functools import *
x=[1,2,3,4,5,6,7]
print(reduce(lambda a,b:a+b,x))
print(list(filter(lambda n:n%2==0,x)))
print(list(map(lambda a:a*2,x)))
from datetime import date
x=date.today()
print(x)





