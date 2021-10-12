#1.Flowchart
a=int(input())
b=int(input())
c=int(input())
d=[a,b,c]
d.sort()
print(d)
#2 Matrix multiplication
import numpy as np
M1=np.random.randint(0,50,(10,5))
print(M1)
M2=np.random.randint(0,50,(5,10))
print(M2)
M3=np.dot(M2, M1)
print(M3)
#3 Pascal triangle
def Pascal_triangle():
    L=[1]
    while True:
        yield L
        L=[1]+[L[i-1]+L[i] for i in range(1,len(L))]+[1]

n=0
for i in Pascal_triangle():
    print(i)
    n+=1
    if n>100:
     break
N=0
for i in Pascal_triangle():
    print(i)
    N+=1
    if N>200:
      break
#4 Add or double
x=int(input())
count=0
while x!=1:
  if x%2==0:
    x/=2
  else:
    x-=1
  count+=1
print(count)
#DynamicProgramming
from itertools import product
m=int(input())
n = 0
for s in product('+-*/ ', repeat = 8):
 e=""

for i in range(1, 9):

 assert(len(s) > 0)

e += '%d' % i

if (s[0] != ' '):

 e += s[0]

s = s[1:]

e += '9'

if eval(e) ==m:

 n += 1

print('%d#' % n, end = '\t')
print('%s=m' % e)