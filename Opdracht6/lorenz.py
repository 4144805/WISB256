from scipy.integrate import odeint
from array import array



class Lorenz(object):
    """textje"""
    def __init__(self,kaas,sigma,rho,beta):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.elements = kaas
    def f(self,X,t):
        [x,y,z] = X
        f = [self.sigma*(y - x), x*(self.rho - z) - y, x*y - (self.beta)*z]
        return f
    def solve(self, T, dt):
        v = []
        m = 0
        while m <= T:
            v.append(m)
            m = m + dt
        u = odeint(self.f,self.elements,v)
        return u
    def __str__(self):
        return str(self.elements)