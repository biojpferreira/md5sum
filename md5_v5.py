# -*- coding: utf-8 -*-
import glob, hashlib
from os import path
from datetime import datetime

data_dia = str(datetime.now().strftime('%d.%m.%y'))
data_hora = str(datetime.now().strftime('Dia: %d/%m/%y -- Ás %H:%M'))  # data e hora de gravação da hash dentro do arquivo final


#função verifica a existencia do arquivo base, lê, gera a hash e escreve em um arquivo txt no diretorio analisado
def producao(formato):
    if path.exists(caminho) == True: #verifica se o caminho apronta para um arquivo txt
        with open(caminho) as lista:
            for line in lista: #Lê cada linha do arquivo
                line = line.rstrip('\n') # remove a quebra de linha
                manipula=(line + formato) #adiciona o caminho mais o tipo de arquivo a ser executado
                if path.exists(line) == True: #verifica se o caminho contido no guia existe
                    for arquivo in glob.glob(manipula, recursive=False): #Para cada arquivo direcionado pelo caminho ele executa o script
                        arquivo = str(arquivo.strip('[]').strip("''")) #Tratamento da string

                        with open(arquivo, 'rb') as md5get: #abre o arquivo a ser lido para o hash
                            data = md5get.read() #leitura do arquivo
                            gerador = hashlib.md5(data).hexdigest() #hash em hexadecimal

                            arq_final = arquivo #colocando o arquivo dentro de outra variavel para conseguidar dar um split sem compromete o resto do codigo
                            if arq_final.split("/")[-1] != ("codigos_md5_"+data_dia+".txt"): # Pega a ultima posição da string no caso o nome do arquivo e verifica se é diferente do nome do arquivo final, caso for ele escreve.
                                arq = open(line + "/codigos_md5_"+data_dia+".txt", "a")  # Abre o arquivo de texto do resultado
                                escritor = ('Arquivo: {} --- Hash: {} --- Data: {}'.format(arquivo, gerador, data_hora)) #Prepara uma variavel para escrever no arquivo final
                                arq.write("\n"+escritor) # Método que escreve a linha do arquivo de resultado
                                arq.close() # fecha o arquivo final
                                if resp_rel == True: relatorio(escritor)

                                print ('Hash realizado com sucesso! " ' + arquivo + r'" ' + data_hora)
                else:#caso o caminho não seja encontrado ele salva um arquivo txt contendo todos os caminhos não encontrados no diretorio atual do usuario
                    print('Caminho não encontrado'+' - '+line+' - '+ data_hora)
                    arq = open ("./caminhos_recusados_"+data_dia+".txt", "a")
                    escritor = ('Caminho não encontrado'+'" '+line+' " '+ data_hora)
                    arq.write("\n"+escritor)
                    arq.close()
                    if resp_rel == True: relatorio(escritor)
                print('\n','='*100,'\n')

    else:
        print ("Você não direcionou um arquivo de texto com os caminhos!")
        exit()

def verificador_formato():
    tipo_arq = str(input('\nQual o tipo de arquivo a ser analisado? [BAM, FASTQ, TODOS]: ')).strip('[]').strip("''").strip().upper() #recebe uma entrada e trata a string para o texto vir limpo

    #Bloco de condição onde se testa se o usuario digitou uma entrada válida e salva em uma variavel pronta para ser usada pelo metodo de produção
    if tipo_arq == 'BAM':
        tipo_arq = ('/*.bam')
        return tipo_arq
    elif tipo_arq == 'FASTQ':
        tipo_arq = ('/*.fastq.gz')
        return tipo_arq
    elif tipo_arq == 'TODOS' or tipo_arq == "" :
        tipo_arq = ('/*.*')
        return tipo_arq
    else:
        print ('Digite uma das opções acima ou contate o bioinformata responsável.')
        verificador_formato()

def relatorio(dado):
        print(dado)
        arq = open("./relatório_md5_" + data_dia + ".txt", "a")
        escritor = ( dado + ' _ ' + data_hora)
        arq.write("\n" + escritor)
        arq.close()

def checa_relatorio():
    rel = str(input('Deseja gerar um relatório dos códigos gerados? [Y,N]')).strip().upper()
    if rel == 'Y':
        return True
    elif rel == 'N':
        return False
    else:
        print ('Digite uma das opções acima ou contate o bioinformata responsável.')
        checa_relatorio()


#variavel 'caminho' contem o caminho do diretório no formato correto
caminho= str(input("""\nQual o caminho de diretório ou do arquivo que contem os caminhos [exclusivamente .TXT]?
 Obs.: Caso já esteja no diretório do arquivo guia digite apenas o seu nome.: """)).strip('[]').strip("''")

if path.exists("./"+caminho) == True:
    caminho = "./"+caminho

print(caminho)

resp_rel = checa_relatorio()

producao(verificador_formato())
