                                        # Curso Python 09


                            # Manipulando Texto (Cadeia de caracteres/string)
#==========================================================================================================

                        # Exemplo de cadeia de caracteres = 'Curso em Vídeo Python'

                                    # frase = Curso em Vídeo Python

# Essa frase tem 21 espaços de memória "[C][u][r][s][o][ ][e][m][ ][V][í][d][e][o][ ][P][y][t][h][o][n]"
#                                        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

    # Fatiamento:

        # frase[9]
        # [9] == [V]

        # frase[9:13]
        # [9:13] == [Víde]

        # frase[9:14]
        # [9:14] == [Vídeo]

        # frase[9:21]
        # [9:21] == [Vídeo Python]

        # frase[9:21:2]
        # [9:21:2] == [VdoPto]
        # considera o caracteres de 2 em 2

        # frase[:5]
        # [:5] == [Curso]
        # do inicio até o 5

        # frase[15:]
        # [15:] == [Python]
        # do [15] até o final

        # frase[9::3]
        # [9::3] == [VePh]
        # do 9 pra cima a cada 3 casas

        # Obs: o último valor não entra na contagem

    # Análise:

        # len(frase)
        # mostra a quantidade de caracteres na (frase) == 21

        # frase.count('o')
        # Quantas vezes existe a letra ó em (frase) == 3

        # frase.count('o',0,13)
        # Quantas vezes existe a letra ó dos caracateres 0 ao 12) == 1

        # frase.find('deo')
        # Quantas vezes ele encontrou "deo" em (frase) == 11

        # 'Curso' in frase
        # Pergunta se existe "Curso" em frase? (true/false)

    # Transformação

        # frase.replace('Python','Android')
        # Substitui "Python" por "Android"

        # frase.upper()
        # Transformar tudo que for minúsculo em maiúsculo

        # frase.lower()
        # Transforma tudo que for maíusculo em minusculo

        # frase.capitalize()
        # Transforma todos os caractéres em minúsculo menos a primeira letra

        # frase.title()
        # Verifica o número de palavras à partir dos espaços e transformará as primeiras letras das palavras em maiúsculo

        # frase.strip()
        # Remove espaços no inicio e final da string
        # frase.rstrip()
        # remove apenas os espaço na direita da string
        # frase.lstrip()
        # remove apenas os espaços na esquerda da string

    # Divisão

        # frase.split()
        # Separa frase em diferentes indexações/listas/cadeia de caracteres ignorando os espaços vazios
        # EX: [C][u][r][s][o][ ][e][m][ ][V][í][d][e][o][ ][P][y][t][h][o][n]
        #      0  1  2  3  4     0  1     0  1  2  3  4     0  1  2  3  4  5
        #            0             1            2                   3

        # '-'.join(frase)
        # Ex de resultado: Curso-em-Vídeo-Python

    # Anotações

        #print('''blabla''') printa independente das quebras de linhas
 # Prática

###frase = 'Curso em Vídeo Python'
####frase.replace('Python', 'Android')
####print(frase)
#printa "Curso em Vídeo Python"
####frase = frase.replace('Python','Android')
####print(frase)
#printa "Curso em Vídeo Android"
####print(frase.find('em')####

# Desafios

    # Desafio022

#Crie um programa que leia o nome completo de uma pessoa e mostre:

    # O nome com todas as letras maiúsculas

    # O nome com todas as mínusculas.

    # Quantas Letras ao todo (sem considerar espaços).

    # Quantas letras tem o primeiro nome.

nome = input('Qual o seu nome completo? ')
print(nome)
print(nome.upper())
print(nome.lower())
#charcount = 0
#for c in nome:
    #if c.isalpha() == True:
        #charcount += 1
#print ('Numero de letras: ' + str(charcount))
print(nome.len[0])



