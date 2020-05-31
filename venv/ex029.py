v = float(input('Qual a velocidade do carro?  '))
if v > 80:
    print('Voce foi multado!')
    r = (v - 80)
    m = (7 * r)
    print('A multa é de R${}'.format(m))
else:
    print('Você é um motorista responsável')
