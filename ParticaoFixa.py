fragmentacao_total = 0


def encontra_primeiro_ads_livre(memoria, tam_memoria):
    for i in range(0, tam_memoria):
        if memoria[i] == '-':
            return i
    return -1


def remove_da_memoria(memoria, tam_memoria, id_processo, particoes, tam_particao):
    processo_em_memoria = False
    count = 0

    for p in particoes:
        if particoes[p][1] == id_processo:
            processo_em_memoria = True
            particoes[p][0] = "Livre"
            particoes[p][1] = "-"
            break

    if not processo_em_memoria:
        print(f"Processo {id_processo} não está na memória!")
        return memoria

    for i in range(0, tam_memoria):
        if memoria[i] == id_processo:
            memoria[i] = '-'
            count += 1

    fragmentacao = tam_particao - count
    global fragmentacao_total
    fragmentacao_total -= fragmentacao

    print(f"Processo {id_processo} removido!")
    print(f"Fragmentação Interna Total: {fragmentacao_total}")
    return memoria


def encontra_primeira_particao_livre(particoes):
    for i in particoes:
        if particoes[i][0] == "Livre":
            return i
    return -1


def insere_na_memoria(memoria, tam_memoria, id_processo, tamanho_processo, particoes, tam_particao):
    # procura o primeiro endereco livre
    particao_livre = encontra_primeira_particao_livre(particoes)

    if particao_livre == -1:
        print(f"Memory Overflow! - Processo {id_processo} não inserido!")
        return memoria

    for i in range(0, tamanho_processo):
        memoria[particao_livre*tam_particao+i] = id_processo

    fragmentacao = tam_particao - tamanho_processo
    global fragmentacao_total
    fragmentacao_total = fragmentacao_total + fragmentacao
    particoes[particao_livre][0] = "Ocupado"
    particoes[particao_livre][1] = id_processo
    print(f"Processo {id_processo} inserido com sucesso!")
    print(f"Fragmentação Interna Total: {fragmentacao_total}")

    return memoria


def imprime_status_memoria(memoria, tam_memoria):
    status_memoria = []
    count = 0
    for i in range(0, tam_memoria):
        if memoria[i] != '-':
            if count != 0:
                status_memoria.append(count)
            count = 0
        elif i == tam_memoria-1 and memoria[i] == '-':
            count += 1
            status_memoria.append(count)
        else:
            count += 1
    print(status_memoria)


def run_particao_fixa(tam_memoria, fila_de_entrada, tam_particao):
    # Inicializa a memoria
    memoria = []
    particoes = {}
    num_particoes = int(tam_memoria/tam_particao)

    for i in range(0, num_particoes):
        particoes[i] = ["Livre", "-"]

    #print(particoes)

    for i in range(0, tam_memoria):
        memoria.append('-')

    # Roda fila de entrada
    print("\n\nINICIO EXECUCAO\n")
    imprime_status_memoria(memoria, tam_memoria)
    for i in fila_de_entrada:

        # Insere ou remove da memoria
        if i[0] == "IN":
            tam_processo = int(i[2])
            nome_processo = i[1]
            if tam_processo > tam_particao:
                print(f"Memory Overflow! - Processo {i[1]} não inserido!")
            else:
                memoria = insere_na_memoria(
                    memoria, tam_memoria, nome_processo, tam_processo, particoes, tam_particao)

        elif i[0] == "OUT":
            memoria = remove_da_memoria(
                memoria, tam_memoria, i[1], particoes, tam_particao)

        imprime_status_memoria(memoria, tam_memoria)
    # Imprime status da memoria
