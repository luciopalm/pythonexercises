frase = str(input('Digite uma frase:')).upper().strip()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A posição que a letra A apareceu pela ultima vez foi: {}'.format(frase.rfind('A')+1))
