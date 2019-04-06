from datetime import datetime # Importa a biblioteca para datas
now = datetime.now()  # Timestamp
content = [] # Conteudo dos arquivos para serem escritos
files = ['file1.txt','file2.txt','file3.txt'] # Nome dos arquivos a serem lidos
for i in files:  # Loop para ler os arquivos e armazenar na var content
    with open(i, 'r') as f:
        content.append(f.read())

name = now.strftime('%Y-%m-%d-%H-%M-%S-%f')+ '.txt' # Colocando como string e nome de arquivo

with open(name, 'w') as f: # Criar e escrever no arquivo alvo
    for i in content:
        f.write(i + '\n')
now_finish = datetime.now()
print('Finalizado! Script levou %s segundos para rodar' % str((now_finish - now).microseconds * 10**-6))
