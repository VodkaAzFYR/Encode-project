from .haszowanie import ntol

def decode(x, k):
     splitted_x = x.split('|')
     z = (splitted_x.pop()) #usuwanie ostatniego boksa
     n = 1
     l_t = ''
     l = ''
     for i in splitted_x:
          if i == '_':   #deszyfracja spacji
               l += ' '
          else:
               i = int(i, 32) #zamiana liczby z systemu 32 na 10
               l_t = i // (k**n)   #deszyfracja liter, cyfr i znakow
               l += ntol(l_t)
               n += 1
     return l