from .haszowanie import lton
from .haszowanie import sys32
def encode(w, z):
    l_t = 0
    n = 1
    l = ''
    for i in w:
        if i == ' ':
            l += str('_') + '|'     #szyfracja spacji
        else:
            l_t = lton(i) * (z ** n)
            l_t = sys32(l_t) #z systemu 10 na 32
            l += str(l_t) + '|'     #szyfracja liter, cyfr i znakow
            n += 1
    return l
