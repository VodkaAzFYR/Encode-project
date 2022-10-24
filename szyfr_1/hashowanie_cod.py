from .haszowanie import sys32
def encode(w, z):
    l_t = 0
    l = ''
    s = 0
    for i in z:
        s += ord(i)
    for i in w:
        l_t = ord(i) * s
        l_t = sys32(l_t) #z systemu 10 na 32
        l += str(l_t) + '|'     #szyfracja liter, cyfr i znakow
    return l
