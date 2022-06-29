from math import inf

def remove_da_memoria(memoria, tam_memoria, id_processo):
    for i in range(0,tam_memoria):
        if memoria[i] == id_processo:
            memoria[i] = '-'

    print(f"Processo {id_processo} removido!")
    return memoria

def encontra_slots_livres(memoria, tam_memoria, tam_processo):
    count = 0
    slots_livres = []
    endereco_inicio = 0

    for i in range(0,tam_memoria):
        if memoria[i] == '-':
            if count == 0:
                endereco_inicio = i

            count += 1
                
            if(i == tam_memoria - 1) and (count >= tam_processo):
                slots_livres.append([endereco_inicio,count])
                
        elif memoria[i] != '-':
            if(count != 0) and (count >= tam_processo):
                slots_livres.append([endereco_inicio,count])	
            count = 0

    return(slots_livres)

def insere_na_memoria(memoria, tam_memoria, id_processo, tamanho_processo, politica):
    # procura o primeiro endereco livre
    slots_livres = encontra_slots_livres(memoria, tam_memoria, tamanho_processo)
    
    if slots_livres == []:
        print(f"Memory Overflow! - Processo {id_processo} não alocado.")
        return memoria
    
    if politica == 1:
        best_fit = slots_livres[0] # best_fit = [endereco_inicio, tamanho_slot]
        dif = inf

        for i in slots_livres:
            if ((i[1] - tamanho_processo) >= 0) and (dif > abs(i[1] - tamanho_processo)):
                dif = abs(i[1] - tamanho_processo)
                best_fit = i

        for i in range(best_fit[0], best_fit[0]+tamanho_processo):
            memoria[i] = id_processo
        print(f"Processo {id_processo} alocado!")

    elif(politica == 2):
        worst_fit = slots_livres[0] # best_fit = [endereco_inicio, tamanho_slot]
        dif = -inf

        for i in slots_livres:
            if ((i[1] - tamanho_processo) >= 0) and (dif < abs(i[1] - tamanho_processo)):
                dif = abs(i[1] - tamanho_processo)
                worst_fit = i

        for i in range(worst_fit[0], worst_fit[0]+tamanho_processo):
            memoria[i] = id_processo
        print(f"Processo {id_processo} alocado!")
    
    return memoria


def imprime_status_memoria(memoria, tam_memoria):
    status_memoria = []
    count = 0
    for i in range(0,tam_memoria):
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

def run_alocacao_dinamica(tam_memoria, fila_de_entrada, politica):
    # Inicializa a memoria
    memoria = []
    for i in range(0,tam_memoria):
        memoria.append('-')
    # Roda fila de entrada
    imprime_status_memoria(memoria, tam_memoria)
    for i in fila_de_entrada:

        # Insere ou remove da memoria
        if i[0] == "IN":
            memoria = insere_na_memoria(memoria, tam_memoria, i[1], int(i[2]), politica)

        elif i[0] == "OUT":
            memoria = remove_da_memoria(memoria, tam_memoria, i[1])

        imprime_status_memoria(memoria, tam_memoria)
    # Imprime status da memoria   
