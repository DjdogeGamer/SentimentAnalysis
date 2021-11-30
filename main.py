from funcoes import *

try:
  arq_pesos = open('pesos.txt', 'r')
except FileNotFoundError:
  print('> O arquivo de pesos não foi encontrado! criando um novo arquivo vazio...')
  arq_pesos = open('pesos.txt', 'r')

try:
  arq_frases = open('frases.txt', 'r')
except FileNotFoundError:
  print('> O arquivo de frases não foi encontrado! criando um novo arquivo vazio...')
  arq_frases = open('frases.txt', 'r')

frases = []
pesos = []

#Tratamento de texto

tratar_texto(arq_frases, frases)
tratar_texto(arq_pesos, pesos)

pesos[0].remove('boas:')
pesos[2].remove('neutras:')
pesos[4].remove('ruims:')

count = 0
arq_pesos = open('frases.txt')
lines = arq_pesos.readlines()
for line in lines:
  print('{} {}'.format(count,line))
  count+=1

index_frase = int(input('Digite qual frase você quer processar: '))

# Contagem de boas, neutras, ruims

palavras_reconhecidas = []
lista_boas = []
palavras_novas = []

# Boas

for i in frases[index_frase]: 
  if i in pesos[0]:
    palavras_reconhecidas.append(i)
    index = (pesos[0].index(i))+1
    valor_boa = pesos[0][index] 
    lista_boas.append(valor_boa)

# Neutras

lista_neutras = []

for i in frases[index_frase]:
  if i in pesos[2]:
    palavras_reconhecidas.append(i)
    index = (pesos[2].index(i))+1
    valor_neutra = pesos[2][index] 
    lista_neutras.append(valor_neutra)

# Ruims

lista_ruims = []

for i in frases[index_frase]:
  if i in pesos[4]:
    palavras_reconhecidas.append(i)
    index = (pesos[4].index(i))+1
    valor_ruim = pesos[4][index] 
    lista_ruims.append(valor_ruim)

# Palavras novas

pesos_tot = pesos[0]+pesos[2]+pesos[4]

for i in frases[index_frase]:
  if i not in pesos_tot:
    palavras_novas.append(i)

# Calculo de Análise de sentimento

qtd_palavras_rec = 0

for i in palavras_reconhecidas:
  qtd_palavras_rec+=1

soma_boas = 0
soma_neutras = 0
soma_ruims = 0

for c in lista_boas: 
  soma_boas+=int(c)

for c in lista_neutras:
  soma_neutras+=int(c)

for c in lista_ruims:
  soma_ruims+=int(c)

media = round((soma_boas+soma_neutras+soma_ruims)/qtd_palavras_rec)

classificacao = ''

if media < 0:
  classificacao = 'Ruim'
if media == 0:
  classificacao = 'Neutra'
if media > 0:
  classificacao = 'Boa'

# Transformar a lista numa frase normal (em string) de novo:

frase_original = ' '.join(str(e) for e in frases[index_frase]) 
res_palavras_reconhecidas = ' '.join(str(e) for e in palavras_reconhecidas)
res_palavras_novas = ' '.join(str(e) for e in palavras_novas)

resultados = [frase_original, res_palavras_reconhecidas, classificacao, res_palavras_novas]

# Algoritmo para aprender novas palavras:

algoritmo = []

for i in palavras_novas:
  algoritmo.append(i)
  algoritmo.append(media)
  algoritmo.append('')

res_algoritmo = ' '.join(str(e) for e in algoritmo) 

with open("pesos.txt", "r") as file:
    texto = file.readlines()

if classificacao == "Ruim":
  texto.insert(4, res_algoritmo)
elif classificacao == "Boa":
  texto.insert(0, res_algoritmo)
elif classificacao == "Neutra":
  texto.insert(2, res_algoritmo)
 
with open("pesos.txt", "w") as file:
    texto = "".join(texto)
    file.write(texto)
print('> Novos pesos adicionados com sucesso! ')

# Contrsução do CSV:

try:
  csv = open('resultados.csv') 
except FileNotFoundError:
  csv = open('resultados.csv', 'a') 
  print('> Arquivo CSV não encontrado! criando um novo aquivo...')
  csv.write('Frase, Lista de palavras reconhecidas, Resultado do cálculo de sentimento, Palavras Aprendidas,')

csv = open('resultados.csv', 'a')
csv.write('\n')
csv.write(resultados[0])
csv.write(', ')
csv.write(resultados[1])
csv.write(', ')
csv.write(resultados[2])
csv.write(', ')
csv.write(resultados[3])
csv.write(', ')
csv.close()
print('> CSV Criado/Atualizado com sucesso! Verifique a saída ')
