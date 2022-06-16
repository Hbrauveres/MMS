from math import inf

def remove_da_memoria(memoria, tam_memoria, id_processo):
    for i in range(0,tam_memoria):
        if memoria[i] == id_processo:
            memoria[i] = '-'

    print("Processo removido!")
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
        print("Processo alocado!")

    elif(politica == 2):
        worst_fit = slots_livres[0] # best_fit = [endereco_inicio, tamanho_slot]
        dif = -inf

        for i in slots_livres:
            if ((i[1] - tamanho_processo) >= 0) and (dif < abs(i[1] - tamanho_processo)):
                dif = abs(i[1] - tamanho_processo)
                worst_fit = i

        for i in range(worst_fit[0], worst_fit[0]+tamanho_processo):
            memoria[i] = id_processo
        print("Processo alocado!")
    
    return memoria



memoria = ['-','-','-','A','-','-','-','-','-','-']
print(memoria)
memoria = insere_na_memoria(memoria, 10, 'X', 2, 1)
print(memoria)
memoria = insere_na_memoria(memoria, 10, 'Y', 3, 1)
print(memoria)
memoria = remove_da_memoria(memoria, 10, 'X')
print(memoria)
memoria = insere_na_memoria(memoria, 10, 'Z', 5, 1)
print(memoria)
memoria = remove_da_memoria(memoria, 10, 'Y')
print(memoria)
memoria = remove_da_memoria(memoria, 10, 'Z')
print(memoria)