n = int(input('Digite um numero inteiro:'))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        t += 1
if t == 2:
    print('PRIMO')
else:
    print('NÃO È PRIMO')