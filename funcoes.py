
def tratar_texto(arquivo, lista):
  for line in arquivo: 
    for i in line:
      line = line.replace("\n","")
      line = line.replace(".","")
      line = line.replace(",","")
      line = line.lower()
    line = line.split()
    lista.append(line)
  return lista
