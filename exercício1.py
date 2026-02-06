""" nome = input('olá viajante qual seu nome?')
print('olá ' + nome +' como vai?')

dia = input('qual o dia em que você nasceu?')
mes = input('em qual mes?')
ano = input('qual ano?')

print('você nasceu no dia ' , dia , ' no mes ' , mes , 'no ano de ' , ano) """


''' colocando como float para pegar o valor para soma, pois se não fizer isso a soma vai ser interpretada como string
n1 = float(input('fala um numero ai'))
n2 = float(input('vai somar com esse'))
soma = n1 + n2
print('a soma entre {} e numero {} é igual a {}' .format(n1, n2, soma) )
'''


'''
Situação:
Você tem um saldo fixo (ex: 100 reais) e quer saber se pode comprar algo.

Regras:

O programa deve:

Definir um saldo inicial (ex: 100)

Perguntar o preço de um produto

Informar se a compra é possível ou não
'''

'''
Regras

Use while

O programa deve:

pedir a resposta

validar a resposta

só sair quando:

a compra acontecer ou

o cliente disser N'''

# valor1 = float(input('quantos reais voce quer filho ')) 
valor1 = 10
bala = float(5) 

print('voce tem {} reais' .format(valor1)) 

resposta = input("ola sou o vendedor, quer comprar uma bala por 5 reais S/N").upper()

while resposta !=  "N" and resposta !=  "S" :
    resposta = input("escreva S ou N por gentileza ").upper()

if (resposta == 'N'): 
    print('certo tenha um otimo dia garoto') 

elif (resposta == 'S') : 
    if valor1 < bala:
        print('voce nao tem dinheiro para comprar bala') 
    else:
        valor1 = valor1 - bala 
        print('toma esta bala garoto')

print('Voce  tem {}  reais' .format(valor1))
