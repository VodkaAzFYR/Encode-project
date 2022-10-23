def lton(x):
    l = '0123456789AĄaąBbCĆcćDdEĘeęFfGgHhIiJjKkŁLlłMmŃNnńÓOoóPpQqRrŚSsśTtUuVvWwXxYyŻŹZzżź,.' #Zbior znakow do szyfracji
    y = l.index(x)
    y += 1
    return y
#print(lton('t'))
#abcdefghijklmnopqrstuvwxyz
#ABCDEFGHIKLMNOPQRSTUXYZ

def ntol(x):
    x = float(x)
    l = '0123456789AĄaąBbCĆcćDdEĘeęFfGgHhIiJjKkŁLlłMmŃNnńÓOoóPpQqRrŚSsśTtUuVvWwXxYyŻŹZzżź,.' #Zbior znakow do deszyfracji
    for i in l:
        if x == float(l.index(i)) + 1:
            return i
#print((ntol(20)))
#123456789abcdefghijklmnopqrstuvwxyz
#123456789AĄaąBbCĆcćDdEĘeęFfGgHhIiJjKkŁLlłMmŃNnńÓOoóPpQqRrŚSsśTtUuVvWwXxYyŻŹZzżź,.
#123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz,.
def sys32_nr(x):
    l = '0123456789abcdefghijklmnopqrstuv'
    for i in l:
        if x == l.index(i):
            return i

def sys32(x):
    y = ''
    while x != 0:
        y += sys32_nr(x%32)
        x = x // 32
    return y[::-1]