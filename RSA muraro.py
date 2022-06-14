def nod(x, y):
    while x > 0:
        tmp = x
        x = y % x
        y = tmp
    return y


def calcE(y):
    for e in range(2, y+1):
        if nod(e, y) == 1:
            return e


def calcD(x, y):
    k = 1
    while k % x != 0:
        k = k + y
        if k % x == 0:
            d = k // x
            return d


p = int(input("Введите простое число p:"))
q = int(input("Введите простое число q:"))
n = p*q
f = (p - 1)*(q-1)
e = calcE(f)
d = calcD(e, f)
print("Открытый ключ:", "{", e, ",", n, "}")
print("Закрытый ключ:", "{", d, ",", n, "}")
m = int(input("Введите сообщение для зашифрования:"))
c = (m**e) % n
print("Зашифрованное сообщение:", c)