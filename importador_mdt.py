import os
import csv
import shutil

#True copiar e colar False vai recortar
copy = False
prefixo = 'MDT-'
#destino Exemplo: "C:\\selecionados" (lembre de criar a pasta antes) 
pasta_destino = "D:\\documentos\\programação\\copia arquivos de lista\\teste"
pasta_origem = "D:\\documentos\\programação\\copia arquivos de lista"
#CSV contendo o nome dos arquivos
arquivo_csv = 'teste.csv'

#pega o nome do arquivo sem a extensão
def getJustFileName(filename):
   fileName, fileExtension = os.path.splitext(filename)
   return fileName

#lista de nomes que arquivos que devem ser copiados/recortados
lista_arquivos = [];

#importa lista de arquivo CSV
with open(arquivo_csv) as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
      lista_arquivos.append(prefixo+row[0])

#print(list_duplicates(lista_arquivos))

contador=0
for root, dirs, files in os.walk(pasta_origem):
    for file in files:
      if file.endswith(".tif"):
        if (getJustFileName(file) in lista_arquivos):
          print(contador, " : ", file)
          if copy != True:
            shutil.move(os.path.join(root, file), pasta_destino+"\\"+file)
          else:
            shutil.copy (os.path.join(root, file), pasta_destino+"\\"+file)
          lista_arquivos.remove(getJustFileName(file))
          contador+=1

print("Arquivos não encontrados: ")
print(lista_arquivos)
