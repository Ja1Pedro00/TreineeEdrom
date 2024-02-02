import os
import shutil

def modifica (pasta, destino):
    
    if not os.path.exists(destino):
        os.makedirs(destino)
        
    for arq in os.listdir(pasta):
        caminho = os.path.join(pasta, arq)
        
        if os.path.isfile(caminho) and arq.endswith(".txt"):
            with open (caminho, 'r') as arquivo:
                linhas = arquivo.readlines()
                
            for i in range(len(linhas)):
                linhas[i] = linhas[i].replace('0', '1', 1)
            
            novo = arq.replace('train', 'ball')
            destino = os.path.join(destino, novo)
            
            with open (destino, 'w') as arquivo:
                arquivo.writelines(linhas)
                
            shutil.move(pasta, destino)
                
        if not os.path.isdir(pasta):
            print(f"local nao encontrado")
            
            return
        
x = input('Digite o caminho do arquivo: ')
y = input("Digite o caminho para o qual o arquivo irá ser transferido: ")
modifica(x, y)
                
        