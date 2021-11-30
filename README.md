# Importar MDT do PE3D
Código para copiar arquivos de lista
Observações:

1) O código foi feito utilizando bibliotecas do python versão 3.6.4, portanto baixar essa versão do python no site: https://www.python.org/downloads/ 

2) O separador de lista do computador tem que estar configurado para vírgula. Conferir em:
Painel de controle > Relógio, Idioma e Região> Região > Alterar formatos de data, hora ou número >  configurações adicionais> separador de lista (,)

3) Exportar o nome das quadrículas desejadas da tabela de atributos do arcgis para o excel

4) Copiar apenas a coluna "nome" para uma planilha excel. Excluir a linha "nome", deixando apenas as linhas com o código das quadrículas. Salvar como extensão csv.

5) Salvar o arquivo csv no mesmo diretório onde está salvo o código. Criar também nesse diretório uma pasta com o nome selecionados.

7) Caso queira  copiar os arquivos deixar a linha 6 do código (copy = True) do jeito que está. Caso queria recortar os arquivos deve-se modificar a linha 6 para
copy = False

7) Caso queira  pesquisar MDEs modificar o prefixo na linha 7 (prefixo = 'MDE-'), caso queria MDT, deixar como está (prefixo = 'MDT-') 

8) Alterar o caminho da pasta onde os arquivos serão copiados. Abrir a pasta selecionados, copiar o endereço e colar entre as aspas.Cuidado, as barras devem ser dupla como mostra o exemplo abaixo.
```
pasta_destino = "D:\\documentos\\programação\\copia arquivos de lista\\teste" (linha 9 do código).
```

9)Definir a pasta onde estão os arquivos a serem pesquisados (pasta contendo todos os MDTs ou MDEs). Copia o endereço da pasta e cola entre as aspas

```
pasta_origem = "D:\\documentos\\programação\\copia arquivos de lista" (linha 10 do código).
```
10)Definir o nome do arquivo csv em que foram salvos a lista com o código das quadrículas selecionadas. O nome tem que estar entre aspas simples e conter a extensão, conforme exemplo abaixo

```
arquivo_csv = 'teste.csv'
```

11)Para rodar o código aperta F5 

12) Se houver arquivos que estão na lista, mas não estão na pasta de todos os MDTs o código irá apresentar ao final os nomes.
