import random
import math
import sys


if len(sys.argv)==4:
    random.seed(float(sys.argv[3]))

if len(sys.argv)<3:
    print('Use: estimate_pi.py N L')
    sys.exit()

N=int(sys.argv[1])
L=float(sys.argv[2])

x=0

def drop_needle(L):
    a=random.random()
    t=random.vonmisesvariate(0,0)
    b=a+L*math.cos(t)
    return not 0<b<1

n=1
while n < N:
    if drop_needle(L):
        x=x+1
    n=n+1

print(str(x)+ ' hits in '+ str(N)+ ' tries')
if L<= 1:
    print('Pi = '+ str(2*L*N/x))
if L>1:
    print('Pi = '+str((2*(L*N-math.sqrt(L**2-1)*N-N*math.asin(1/L)))/(x-N)))