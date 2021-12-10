#Exercício 36
# casa = float(input('Valor da Casa: '))
# salario = float(input('Salário do Comprador: '))
# anos = int(input('Quantos anos de financiamento: '))
# prestacao = casa / (anos * 12)
# minimo = salario * 30/100
# print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos))
# print('A prestação será de R${:.2f} '.format(prestacao))
# if prestacao <= minimo:
#     print('Empréstimo pode ser CONCEDIDO! ')
# else:
#     print('Empréstimo NEGADO ')

#Exercício 37
# valor = int(input('Digite um número inteiro : '))
# print('''Escolha uma das bases para conversão:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL''')
# opção = int(input('Sua opção: '))
# if opção == 1:
#     print('{} convertido para BINÁRIO é igual a {} '.format(valor, bin(valor) [2:] ))
# elif opção == 2:
#     print('{} convertito para OCTAL é igual a {} '.format(valor, oct(valor) [2:] ))
# elif opção == 3:
#     print('{} convertido para HEXADECIMAL é igual a {} '.format(valor, hex(valor) [2:] ))
# else:
#     print('Opção inválida. Tente novamente.')

#Exercício 38
# num = int(input('Primeiro número: '))
# num2 = int(input('Segundo número: '))
# if num > num2:
#     print('O PRIMEIRO valor é maior')
# elif num < num2:
#     print('O SEGUNDO valor é maior')
# else:
#     print('Os dois valores são IGUAIS')

#Exercício 39
# from datetime import  date
# atual = date.today().year
# ano = int(input('Ano de Nascimento:'))
# idade= atual - ano
# print('Quem nasceu {} tem {} anos em {} '.format(ano, idade, atual))
# if idade == 18:
#     print('Você tem que se alistar IMEDIATAMENTE')
# elif idade < 18:
#     saldo = 18 - idade
#     ano = atual + saldo
#     print('Ainda falta {} anos pro Alistamento'.format(saldo))
#     print('Seu alistamento vai ser em {}'.format(ano))
# else:
#     saldo = idade - 18
#     ano = atual - saldo
#     print('Você já devia ter se alistado há {} anos'.format(saldo))
#     print('Seu alistamento foi em {}'.format(ano))

# Exercício 40
# nota1 = float(input('Primeira Nota: '))
# nota2 = float(input('Segundo Nota: '))
# media = (nota1 + nota2) / 2
# if media > 7.0:
#     print('Tirando {} e {}, a média do aluno é {}. O aluno foi APROVADO'.format(nota1, nota2, media))
# elif media == 5.0 or media < 7.0:
#     print('Tirando {} e {}, a média do aluno é {}. Ele está em RECUPERAÇÃO'.format(nota1, nota2, media))
# else:
#     print('Tirando {} e {}, a média do aluno é {}. O aluno foi REPROVADO'.format(nota1, nota2, media))

# Exercício 41
# from datetime import date
# atual = date.today().year
# ano = int(input('Ano de Nascimento: '))
# idade = atual - ano
# if atual <= 9:
#     print('Você tem {} anos, então você é MIRIM '.format(idade))
# elif idade <= 14:
#     print('A partir dos {} anos, você é INFANTIS '.format(idade))
# elif  idade <= 19:
#     print('Parabéns com {} anos, agora você é JÚNIOR'.format(idade))
# elif idade <= 25:
#     print('Parabéns agora que tu tens {} anos, vc é SÊNIOR '.format(idade))
# else:
#     print('A partir de agora você é master, pois possui {} anos'.format(idade))

# Exercício 42
# print('-=-' * 20)
# print('Analisador de Triângulos')
# print('-=-' * 20)
#
# r1 = float(input('Primeiro Segmento: '))
# r2 = float(input('Segundo Segmento: '))
# r3 = float(input('Terceiro Segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os SEGMENTOS acima PODEM formar um TRIÂNGULO')
#     if r1 == r2 and r2 == r3:
#         print('EQUILÁTERO.')
#     if r1 != r2 != r3:
#         print('ESCALENO!')
#     if r1 == r2 != r3:
#         print('ISÓSCELES')
# else:
#     print('Os SEGMENTOS acima NÃO podem formar um TRIÂNGULO')

# Exercício 43
# peso = float(input(' Qual é o seu peso? (KG) '))
# altura = float(input('Qual é a sua altura? (M)'))
# IMC = peso / (altura ** 2)
# print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
# if IMC < 18.5:
#     print('Você está ABAIXO DO PESO RECOMENDADO!')
#
# elif IMC >= 18.5 and IMC < 25:
#     print('Parabéns você está no PESO IDEAL!')
#
# elif 25 <= IMC < 30:
#     print('Você está em SOBREPESO')
#
# elif 30 <= IMC < 40:
#     print('Você ficou com OBESIDADE, trate-se')
#
# else:
#     print('Você está em OBESIDADE MÓRBIDA, cuidado!')

# Exercício 44

# print('{:=^40}'.format(' LOJAS GAMERS NICE '))
# preço = float(input('Preço das compras: R$ '))
# print('''FORMAS DE PAGAMENTO
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista no cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão''')
# opção = int(input('Qual é a opção? '))
# if opção == 1:
#     total = preço - (preço * 10/100)
# elif opção == 2:
#     total = preço - (preço * 5/100)
# elif opção == 3:
#     total = preço
#     parcela = total / 2
#     print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS '.format(parcela))
# else:
#     total = preço + (preço * 20/100)
#     totparc = int(input('Quantas parcelas ? '))
#     parcela = total / totparc
#     print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totparc, parcela))
# print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preço, total))

# Exercício 45
from random import  randint
from  time import  sleep
Itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou {} '.format(Itens[computador]))
print('Jogador jogou {} '.format(Itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('\033[7;33;44mEMPATE\033[m')
    elif jogador == 1:
        print('\033[3;30mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[4;27mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[8;39;42mJogada Inválida\033[m')

elif computador == 1:
    if jogador == 0:
        print('\033[4;37;40mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[7;33;44mEMPATE\033[m')
    elif jogador == 2:
        print('\033[3;30mJOGADOR VENCEU\033[m')
    else:
        print('\033[8;39;42mJogada Inválida\033[m')

elif computador == 2:
    if jogador == 0:
        print('\033[3;30mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[4;37;40mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[7;33;44mEMPATE\033[m')
    else:
        print('\033[8;39;42mJogada Inválida\033[m')