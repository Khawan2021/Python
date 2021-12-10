#Aula 12
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Khawan':
#     print('Que nome bonito!')
# elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'João':
#     print('Seu nome é bem popular no Brasil.')
# elif nome in 'Ana Claúdia Jéssica Juliana':
#     print('Belo nome feminino')
# else:
#     print('Seu nome é bem normal')
# print('Tenha um bom dia {}!'.format(nome))

# Aula 13
# for c in range(0, 6):
#     print('Oi')
# print('FIM')

# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))