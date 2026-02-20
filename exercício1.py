""" perguntar e mostrar o dia o mes e o ano do usuario"""
nome = input('olá viajante qual seu nome?')
print('olá ' + nome +' como vai?')

dia = input('qual o dia em que você nasceu?')
mes = input('em qual mes?')
ano = input('qual ano?')

print('você nasceu no dia ' , dia , ' no mes ' , mes , 'no ano de ' , ano)


''' colocando como float para pegar o valor para soma, pois se não fizer isso a soma vai ser interpretada como string'''

n1 = float(input('fala um numero ai'))
n2 = float(input('vai somar com esse'))
soma = n1 + n2
print('a soma entre {} e numero {} é igual a {}' .format(n1, n2, soma) )



