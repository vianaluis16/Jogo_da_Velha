import random
from os import system, name


def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "20191019126"


def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "LUIS VIANA"


def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


###################################################################################
# (1) Crie uma função que solicite a letra que o jogador deve ser.                 #
# A função retorna dois valores. Se o jogador desejar ser "X", retorne "X", "O". #
# Caso contrário, retorne "O", "X".                                               #
###################################################################################
def simbolos():
    simbolo = input("Escolha com qual simbolo vai jogar: ")
    if simbolo == "X":
        return "X", "O"
    elif simbolo == "O":
        return "O", "X"
    else:
        print("Escolha apenas X ou O.")
        return simbolos()


###################################################################################
# (2) Crie uma função que decida/retorna quem será o primeiro a jogar.             #
# Use o módulo random.                                                            #
###################################################################################
def primeiro():
    return random.choice(["Jogador", "Computador"])


###################################################################################
# (3) Crie uma função para imprimir o tabuleiro.                                   #
# Função não retorna nada, apenas imprime.                                        #
###################################################################################
def desenhotabuleiro(tabuleiro):
    print(f"  {tabuleiro[7]} |  {tabuleiro[8]}  | {tabuleiro[9]} ")
    print(f"----+-----+----")
    print(f"  {tabuleiro[4]} |  {tabuleiro[5]}  | {tabuleiro[6]} ")
    print(f"----+-----+----")
    print(f"  {tabuleiro[1]} |  {tabuleiro[2]}  | {tabuleiro[3]} ")


###################################################################################
# (4) Faça uma função que solicite ao usuário onde ele deseja jogar.               #
# A função retorna um inteiro entre 1 e 9 (posicão escolhida)                     #
# A função deve garantir que o usuários selecionou uma posição válida             #
###################################################################################
def jogouAonde():
    jogada = int(input("Escolha onde jogar: "))
    if jogada > 9 or jogada < 1:
        print("posicao invalida")
        return jogouAonde()
    else:
        return jogada


###################################################################################
# (5) Faça uma função que retorna True se o "X" ou "O" ganhou e False, caso        #
# contrário. A função deve receber o tabuleiro e o simbolo a ser testado.         #
# Verifique todas as possibilidades e retorne True caso uma delas o simbolo       #
# ganhou. Por exemplo, se nas posições 7, 8 e 9 do tabuleiro contém "X",          #
# significa que "X" ganhou e a função deve retornar True.                         #
###################################################################################

def ganhou(tabuleiro, simbolo):
    if tabuleiro[1] == simbolo and tabuleiro[2] == simbolo and tabuleiro[3] == simbolo:
        return True
    elif tabuleiro[4] == simbolo and tabuleiro[5] == simbolo and tabuleiro[6] == simbolo:
        return True
    elif tabuleiro[7] == simbolo and tabuleiro[8] == simbolo and tabuleiro[9] == simbolo:
        return True
    elif tabuleiro[1] == simbolo and tabuleiro[4] == simbolo and tabuleiro[7] == simbolo:
        return True
    elif tabuleiro[2] == simbolo and tabuleiro[5] == simbolo and tabuleiro[8] == simbolo:
        return True
    elif tabuleiro[3] == simbolo and tabuleiro[6] == simbolo and tabuleiro[9] == simbolo:
        return True
    elif tabuleiro[1] == simbolo and tabuleiro[5] == simbolo and tabuleiro[9] == simbolo:
        return True
    elif tabuleiro[7] == simbolo and tabuleiro[5] == simbolo and tabuleiro[3] == simbolo:
        return True
    else:
        return False


###################################################################################
# (6) Faça uma função que retorne True se houve empate e False, caso contrário.    #
# Para isso, basta verificar se o tabuleiro está todo preenchido, ou seja, não    #
# contém nenhum espaço em branco.                                                 #
###################################################################################
def empate(tabuleiro):
    if tabuleiro[1] == " " or tabuleiro[2] == " " or tabuleiro[3] == " " or tabuleiro[4] == " " or tabuleiro[
        5] == " " or tabuleiro[6] == " " or tabuleiro[7] == " " or tabuleiro[8] == " " or tabuleiro[9] == " ":
        return False
    else:
        return True


###################################################################################
# (7.1) Faça uma função que receba o tabuleiro e retorne as posições, entre 1 e 9  #
# que estão livres                                                                #
###################################################################################
def posicoesLivres(tabuleiro):
    return [i for i in range(1, len(tabuleiro)) if tabuleiro[i] == " "]


###################################################################################
# (7.2) Faça uma função que receba o tabuleiro, escolha (aleatoriamente) e retorne #
# uma posição livre. Use a função (7.1).
###################################################################################
def posicaoRandom(tabuleiro):
    return random.choice(posicoesLivres(tabuleiro))


###################################################################################
# (8) Começa a implementar a função jogadaComputador. De início, você pode apenas  #
# sortear uma posição livre como sendo a jogada do computador. Use a função (7.2) #
# Posteriormente, implemente alguma estratégia mais  "inteligente".               #
###################################################################################
def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas,
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador
    """
    y = random.choice([x for x in range(1, len(tabuleiro)) if tabuleiro[x] == " "])
    print(y)
    tabuleiro[y] = simboloComputador
    return tabuleiro[y]


###################################################################################
# (9) Faça uma função que será responsável pelas jogadas, intercalando entre o     #
# jogador e o computador. Essa função, caso queira, pode retornar quem venceu ou  #
# se o jogo terminou empatado. Note que essas função deve ser recursiva, ou seja, #
# ela deve ser chamada recursivamente para cada jogada enquanto não houver        #
# vencedor ou empate.                                                             #
# Sugestão de parâmetros obrigatórios para essa função:                            #
# - Tabuleiro                                                                     #
# - De quem é a vez da jogada                                                     #
# - Simbolo do jogador                                                            #
# - Simbolo do computador                                                         #
###################################################################################
def coracao(tabuleiro, primeiroJoga, simboloJogador, simboloComputador, i=1):
    if len(tabuleiro) == i:
        print("algm ganhou ou empatou")
    else:
        if primeiroJoga == "Jogador":
            x = int(input("Escolha onde jogar: "))
            if tabuleiro[x] == " ":
                tabuleiro[x] = simboloJogador
                return coracao(tabuleiro, "Computador", simboloJogador, simboloComputador, i + 1)
            else:
                print("Jogue em posições livres.")
                return coracao(tabuleiro, primeiroJoga, simboloJogador, simboloComputador, i)
        else:
            y = random.choice([x for x in range(1, len(tabuleiro)) if tabuleiro[x] == " "])
            print(y)
            tabuleiro[y] = simboloComputador
            return coracao(tabuleiro, "Jogador", simboloJogador, simboloComputador, i + 1)


def main():
    limpaTela()
    # (10) Mensagem de boas-vindas :)
    print("Bem-vindo ao clássico Jogo da Velha!!!")

    # (11) Cria o tabuleiro (uma lista de tamanho 10, inicialmente vazia).
    # Escolha algum simbolo para representar que determinada posição está vazia.
    # Minha sugestão é "" ou " ", mas sinta-se a vontade para escolher o simbolo
    # que achar melhor.
    desenhaTabuleiro([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

    # (12) Chame a função (1) e atribua o resultado a duas variáveis. Uma irá representar
    # o simbolo do jogador e a outra o simbolo do computador.
    if simbolos() == ("X", "O"):
        simboloJogador = "X"
        simboloComputador = "O"
    else:
        simboloJogador = "O"
        simboloComputador = "X"

    # (13) Chame a função (2) e atribua o resultado a um variável que representa quem
    # começa jogando.
    # Imprima quem irá começar a partida.
    print(f"O {primeiro()} começa.")

    # (14) Chame a função (9)
    coracao()

if __name__ == "__main__":
    main()