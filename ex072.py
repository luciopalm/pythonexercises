ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if n > 20:
        print('ERRO DE DIGITAÇÃO - Digite novamente!')
    else:
        break
print(ext[n])



