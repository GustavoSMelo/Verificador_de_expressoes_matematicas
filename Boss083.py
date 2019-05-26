print('=' * 30)
print('Boss 83 meio dificil python ')
print('=' * 30)

verificador = []
expressao = str(input('\nDigite qualquer expressão matematica \nE verifique se ela é verdadeira: '))
abertura = int(0)
fechamento = int(0)

for c in range(0, len(expressao)):
    verificador.append(expressao[c])

abertura = verificador.count('(')
fechamento = verificador.count(')')

if(abertura == fechamento):
    print('Expressão valida! ')

elif(abertura > fechamento):
    print('Expressão invalida! ')

elif(abertura < fechamento):
    print('Expressão invalida! ')

input('Fim da aplicação, pressione ENTER para continuar... ')
