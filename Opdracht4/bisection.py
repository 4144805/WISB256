def findRoot(f,a,b,e):
    m=(b+a)/2
    if abs(a-b)<=e:
        return m
    if f(a)<=0<=f(m) or f(a)>=0>=f(m):
        return findRoot(f,a,m,e)
    if f(m)<=0<=f(b) or f(m)>=0>=f(b):
        return findRoot(f,m,b,e)
        
        
lijst = []

def findAllRoots1(f,a,b,e):
    m=(b+a)/2
    if abs(a-b)<=e:
        return m
    if (f(a)<=0<=f(m) or f(a)>=0>=f(m)) and (f(m)<=0<=f(b) or f(m)>=0>=f(b)):
        lijst.append(findAllRoots1(f,m,b,e))
        return findAllRoots1(f,a,m,e)
    elif f(a)<=0<=f(m) or f(a)>=0>=f(m):
        return findAllRoots1(f,a,m,e)
    elif f(m)<=0<=f(b) or f(m)>=0>=f(b):
        return findAllRoots1(f,m,b,e)

def findAllRoots(f,a,b,e):
    lijst.append(findAllRoots1(f,a,b,e))
    return lijst