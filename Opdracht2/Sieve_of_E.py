import time
import sys
N=int(sys.argv[1])
f=open(sys.argv[2],'w')
T1=time.perf_counter()
l=list(range(0, N+1))
x=2
while x < N:
    k = 2
    while x*k < N+1:
        l[x*k]=0
        k=k+1
    x=x+1
l=list(set(l))
l.remove(0)
l.remove(1)
l.sort()
for x in l:
    f.write(str(x)+'\n')
T2=time.perf_counter()
print('Found '+str(len(l))+' Primes smaller than '+str(N)+' in', T2 - T1,'sec.')