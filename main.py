import os
import ParticaoFixa as PF
import AlocacaoDinamica as AD
import Buddy as BD


def potencia_de_dois(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n / 2
    return True


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def tamanho_particao_valido(tam_particao, tam_memoria):
    if tam_memoria % tam_particao == 0:
        return True
    else:
        return False


def main():
    # Cria fila de entradas
    fila_de_entrada = []

    # Pergunta o nome do arquivo
    # clear_terminal()
    nome_arquivo = input("Informe o nome do arquivo:\n> ")

    # Abre o arquivo e carrega na fila de entrada
    # clear_terminal()
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            fila_de_entrada.append(linha.replace(",", "").replace(
                "(", " ").replace(")", "").split())
            #print(fila_de_entrada)

    # Pergunta o tipo de particionamento
    tipo_particionamento = -1
    while(tipo_particionamento != 1 and tipo_particionamento != 2 and tipo_particionamento != 3):
        # clear_terminal()
        tipo_particionamento = int(input(
            "Informe o tipo de particionamento:\n[1] Particao Fixa\n[2] Particao Variavel\n[3] Particao Buddy\n> "))

    # Pergunta o tamanho da memoria
    tamanho_memoria = -1
    while(1):
        # clear_terminal()
        tamanho_memoria = int(input("Informe o tamanho da memoria:\n> "))
        if potencia_de_dois(tamanho_memoria) == False:
                input(
                "Tamanho da memoria deve ser potencia de dois!\nPressione enter para continuar...")
        else:
            # clear_terminal()
            break

    #Caso seja particionamento dinâmico, pergunta a política (best-fit ou worst-fit)      
    politica = -1
    if tipo_particionamento == 2:
        while(politica != 1 and politica != 2):
            # clear_terminal()
            politica = int(
                input("Informe a politica:\n[1] Best Fit\n[2] Worst Fit\n> "))
            if politica != 1 and politica != 2:
                    input(
                    "Politica incorreta!\nPressione enter para continuar...")
            else:
                # clear_terminal()
                break


    #Caso seja particionamento fixo, pergunta o tamanho da partição
    tamanho_particao = -1
    if tipo_particionamento == 1:
        while(1):
            tamanho_particao = input("Informe o tamanho da particao:\n> ")
            if tamanho_particao_valido(int(tamanho_particao), tamanho_memoria) and tamanho_particao.isnumeric():
                tamanho_particao = int(tamanho_particao)
                break
            else:
                input(
                    "Tamanho de partição invalido!\n\nPressione enter para continuar...")

    # Chama o tipo de particionamento
    if tipo_particionamento == 1:
        PF.run_particao_fixa(
            tamanho_memoria, fila_de_entrada, tamanho_particao)
    elif tipo_particionamento == 2:
        AD.run_alocacao_dinamica(
            tamanho_memoria, fila_de_entrada, politica)
    elif tipo_particionamento == 3:
        BD.run_buddy_system(tamanho_memoria, fila_de_entrada)

    restart_flag = -1
    while(restart_flag != 0 and restart_flag != 1):
        restart_flag = int(
            input("Deseja reiniciar o programa?\n[1] Sim\n[0] Não\n> "))
        clear_terminal()

    if restart_flag == 0:
        exit()
    else:
        main()


if __name__ == "__main__":
    main()
