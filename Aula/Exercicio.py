# import math
# import random

# Exercício 1
# aluno1 = str(input('Primeiro aluno : '))
# aluno2 = str(input('Segundo aluno : '))
# aluno3 = str(input('Terceiro aluno : '))
# aluno4 = str(input('Quarto aluno : '))
# lista = [aluno1,aluno2,aluno3,aluno4]
# escolhido = random.choice(lista)
# print('O aluno escolhido foi [{}]'.format(lista))

# Exercício 2
# an = float(input('Digite um angulo : '))
# seno = math.sin(math.radians(an))
# coseno = math.cos(math.radians(an))
# tangente = math.tan(math.radians(an))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, coseno))
# print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))

# Exercício 3
# num = float(input('Digite um número : '))
# real = math.floor(num)
# print('O número {} tem a parte inteira {}'.format(num, math.floor(real)))

# Exercício 4
# co = float(input('Comprimento do cateto oposto : '))
# ca = float(input('Comprimento do cateto adjacente : '))
# hi = math.hypot(co,ca)
# print('A medida da hipotenusa é {:.2f} '.format(hi))

# Exercício 5
# co = float(input('Entre com o valor do cateto oposto: '))
# ca = float(input('Entre com o valor do cateto adjacente: '))
#
# hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
#
# print("\n**************************\n")
#
# print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))

# Exercício 6
#n1 = int(input('Digite um número:'))
#n2= int(input('Digite mais um número:'))
#s= n1 + n2
#print('A soma de {} e {} vale {}'.format(n1,n2, s))

# Exercício 7
#n= input('Digite um valor: ')
#print('Esse é um número',n.isalnum())
#print('número decimal é',n.isdecimal())
#print('Tem a letra',n.isalpha())
#print('Está em maiusculo',n.isupper())
#print('númerico', n.isnumeric())
#print('---',n.isascii())
#print('--',n.isdigit())
#print("-",n.isidentifier())
#print(type(n))

# Exercício 8
# #n= int(input('Digite um número: '))
# print('número sucessor {}'.format(n + 1))
# print('número antecessor {}'.format(n - 1))

# Exercício 9
# n = int(input('Digite um número: '))
# print('Meu dobro do número é {}'.format(n*2))
# print('Meu triplo do número é {}'.format(n*3))
# print('Minha raíz quadrada é {}'.format(n**(1/2)))

# Exercício 10
# n = float(input('Primeira nota: '))
# n2= float(input('Segunda nota: '))
# print('A nota do aluno é {}'.format((n + n2) / 2))

# Exercício 11
# n = float(input('Número em metros: '))
# print('Número convertido em cm {} e mm {}'.format(n * 100, n * 1000))

# Exercício 12
# n = int(input('tabuada de números: '))
# print('tabuada do número {}. {} {} {} {} {} {} {} {} {} {} '.format(n,n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10))

# Exercício 13
# n= float(input('Minha carteira : '))
# print('O valor de reais convertido em dolar é {:.2f} '.format(n/5.11))

# Exercício 14
# largura = float(input('Digite a largura: '))
# # altura = float(input('Digite a altura: '))
# # area = altura * largura
# # print('Minha área em metros é {}. A tinta necessária é {}'.format(area, area/2))

# Exercício 15
# n = float(input('Digite um preço: '))
# print('O novo preço é {:.2f}'.format(n-(n*0.05)))

# Exercício 16
# salario = float(input('Salário atual: '))
# print('O novo salário é {} '.format(salario+(salario*(15/100))))

# Exercício 17
# grau = float(input('Temperatura atual ºC: '))
# print('Foi convertido em {} ºF'.format(grau*1.8 + 32))

# Exercício 18
# c = float(input('Temperatura em ºC: '))
# f = ((9*c)/5)+32
# print('O valor em {} ºC foi convertido em {} ºF'.format(c, f))

# Exercício 19
# c = float(input('Quantidade de Km percorrido: '))
# d = int(input('Quantidade de dias que o carro foi alugado: '))
# paga = (d * 60) + (c * 0.15)
# print('O total a paga é de R${:.2f}'.format(paga))

# Exercício 20
# frase = 'Beiramar Nutela Raiz'
# print(frase.upper())
# print(frase.lower())
# print(frase.split())
# print(len(frase.strip()))
# print(len(frase.strip('Beiramar')))

# Exercício 22
# nome = str(input('Digite o seu nome: ')).strip()
# print('Analisando seu nome...')
# print('Seu nome em maiuscúlo é {}'.format(nome.upper()))
# print('Seu nome em minuscúlo é {}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))

# Exercício 23
# num = int(input('Informe o seu número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))

# Exercício 24
# cid = str(input('Em que cidade você nasceu ? ')).strip()
# print(cid[:5].upper() == 'SANTO')
# cid = str('Joãozinho Mono Yasuo').strip()
# print(cid[:5].upper() == 'MONO')

# Exercício 25
# nome = str(input('Qual seu nome completo? '))
# print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

# Exercício 26
# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
# print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

# Exercício 27
# n = str(input('Digite um nome: ')).strip()
# nome = n.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))

# Exercício 28
# from random import  randint
# import time
# computador = randint(0, 5)
# print('-==-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-==-' * 20)
# jogador = int(input('Em que número eu pensei? '))
# print('PROCESSANDO...')
# time.sleep(2)
# if jogador == computador:
#     print('Parabéns você me venceu!')
# else:
#     print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))

# Exercício 29
# velocidade = float(input('Qual é a velocidade atual do carro?'))
# if velocidade > 80:
#     print('MULTADO! Você exedeu o limite permitido que é 80Km/H')
#     multa = (velocidade-80)*7
#     print('Você deve pagar uma multa de R${:.2f}'.format(multa))
# print('Tenha um bom dia! Diriga com segurança! ')

# Exercício 30
# num = int(input('Me diga um número qualquer: '))
# resultado = num % 2
# if resultado == 0:
#     print('O número {} é PAR'.format(num))
# else:
#     print('O número {} é IMPAR'.format(num))

# Exercício 31
# distancia = float(input('Qual é a distância da sua viagem? '))
# print('Você está a começar uma viagem de {}Km.'.format(distancia))
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# # if distancia <= 200:
# #     preco = distancia * 0.50
# # else:
# #     preco = distancia * 0.45
# print('E o preço da sua passagem será R${:.2f}'.format(preco))

# Exercício 32
# from datetime import date
# ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
# if ano == 0:
#     date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} NÃO é BISSEXTO'.format(ano))

# Exercício 33
# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
#Vereficando se o número é menor
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c

#Vereficando se o número é maior
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print('O menor valor digitado foi {}'.format(menor))
# print('O maior valor digitado foi {}'.format(maior))

# Exercício 34
# salario = float(input('Qual é o salário do funcionário? R$'))
# if salario <= 1250:
#     novo = salario + (salario * 15 / 100)
# else:
#     novo = salario + (salario * 10 / 100)
# print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora'.format(salario, novo))

# Exercício 35
# print('-=-' * 20)
# print('Analisador de Triângulos')
# print('-=-' * 20)
#
# r1 = float(input('Primeiro Segmento: '))
# r2 = float(input('Segundo Segmento: '))
# r3 = float(input('Terceiro Segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os SEGMENTOS acima PODEM formar um TRIÂNGULO')
# else:
#     print('Os SEGMENTOS acima NÃO podem formar um TRIÂNGULO')