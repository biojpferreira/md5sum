# jptools
Pacote de ferramentas bioinformáticas

* md5_v5.py (Gerador de hash's para arquivos FASTQ, BAM ou todos)

## Itens necessários para o funcionamento do script gerador de hash MD5:
* Python 3.6.8

## Workflow
1. Crie um arquivo txt contendo todos os caminhos dos diretórios a serem analisados.
2. Execute o script.
3. Passe o caminho do arquivo txt criado.
4. Escolha o tipo de arquivo a ser analizado.
5. Defina sim ou não para geração de relatório.
6. Ao final do script será gerado um arquivo txt em cada diretório analisado contendo as hash's juntamente com o nome do arquivo.
No caso da opção de geração de relatório será criado um arquivo txt contendo todos as hash's no diretório no qual o script foi inicializado.

## Instalação
 
## Como executar:
```bash
#Criando arquivo guia.
ls -1d /home/brokssord/Desktop/testes_python/teste_funcional/* > guia.txt

#executando script.
/home/brokssord/Desktop/testes_python/md5_v5.py

Deseja gerar um relatório dos códigos gerados? [Y,N]y

Qual o tipo de arquivo a ser analisado? [BAM, FASTQ, TODOS]: 
Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio/da.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio/da.txt" Dia: 25/10/19 -- Ás 10:54
Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio/daaa.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio/daaa.txt" Dia: 25/10/19 -- Ás 10:54

 ==================================================================================================== 

Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio2/ca.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio2/ca.txt" Dia: 25/10/19 -- Ás 10:54
Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio2/df.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio2/df.txt" Dia: 25/10/19 -- Ás 10:54

 ==================================================================================================== 

Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/ba.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/ba.txt" Dia: 25/10/19 -- Ás 10:54
Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/aa.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/aa.txt" Dia: 25/10/19 -- Ás 10:54
Arquivo: /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/df.txt --- Hash: d41d8cd98f00b204e9800998ecf8427e --- Data: Dia: 25/10/19 -- Ás 10:54
Hash realizado com sucesso! " /home/brokssord/Desktop/testes_python/teste_funcional/diretorio3/df.txt" Dia: 25/10/19 -- Ás 10:54

 ==================================================================================================== 


```
