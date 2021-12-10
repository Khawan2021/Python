import pandas as pd
import win32com.client as win32
# importar a base de dados
tabela_vendas = pd.read_excel("Vendas.xlsx")

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)
print('-' * 50)

# Faturamento por loja
Faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(Faturamento)

# Quantidade de produtos vendidos por loja
Quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(Quantidade)
print('-' * 50)

# ticket médio por produto em cada loja
ticket_medio= (Faturamento['Valor Final'] / Quantidade['Quantidade']).to_frame()
ticket_medio =ticket_medio.rename(columns={0:'Ticket Médio'})
print(ticket_medio)
print('-' * 50)

# enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'khawan.bispo@gmail.com'
mail.Subject ='Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada loja.</p>

<p>Faturamento:</p>
{Faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{Quantidade.to_html()}

<p>Ticket médio dos Produto em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou a disposição.</p>
<p>att..,</p>
<p>Khawan</p>
'''

mail.Send()
print('Email enviado')