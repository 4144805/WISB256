class Vector(object):
    """Represents a vector in n-D space
    
    attributes: number, elements
    """
    def __init__(self, n, kaas = float(0)):
        self.number = n
        self.elements = []
        if isinstance(kaas,float):
            m = 1
            while m <= n:
                self.elements.append(kaas)
                m = m + 1
        if isinstance(kaas,list):
            m = 0
            while m <= n - 1:
                self.elements.append(kaas[m])
                m = m + 1
    def lincomb(self,other,a,b):
        vecci = []
        m = 0
        while m <= self.number - 1:
            vecci.append(a*self.elements[m] + b*other.elements[m])
            m = m + 1
        return Vector(len(vecci),vecci)
    def scalar(self,a):
        vecci = []
        m = 0
        while m <= self.number - 1:
            vecci.append(a*self.elements[m])
            m = m + 1
        return Vector(len(vecci), vecci)
    def inner(self,other):
        sommekke = 0
        m = 0
        while m <= self.number - 1:
            sommekke = sommekke + self.elements[m] + other.elements[m]
            m = m + 1
        return sommekke
    def norm(self):
        sommekke = 0
        m = 0
        while m <= self.number - 1:
            sommekke = sommekke + self.elements[m]**2
            m = m + 1
        return sommekke**(1/2)
    def __str__(self):
        quorp = []
        m = 0
        while m <= self.number - 2:
            quorp.append(self.elements[m])
            m = m + 1
        return int(self.number - 1)*'%g \n'  % tuple(quorp) + '%g' % self.elements[self.number - 1]
    
