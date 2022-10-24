
def decode(x, k):
     splitted_x = x.split('|')
     z = (splitted_x.pop()) #usuwanie ostatniego boksa
     l_t = ''
     l = ''
     s = 0
     for i in k:
          s += ord(i)
     for i in splitted_x:
          i = int(i, 32) #zamiana liczby z systemu 32 na 10
          l_t = i // s  #deszyfracja liter, cyfr i znakow
          l += chr(l_t)
     return l
