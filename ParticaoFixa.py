def encontra_primeiro_ads_livre(memoria, tam_memoria):
    for i in range(0,tam_memoria):
        if memoria[i] == '-':
            return i
    return -1

def remove_da_memoria(memoria, tam_memoria, id_processo):
    for i in range(0,tam_memoria):
        if memoria[i] == id_processo:
            memoria[i] = '-'
    
    print("Processo removido!")
    return memoria

def insere_na_memoria(memoria, tam_memoria, id_processo, tamanho_processo):
    # procura o primeiro endereco livre
    endereco_livre = encontra_primeiro_ads_livre(memoria, tam_memoria)
    count = 0
    for i in range(endereco_livre,tam_memoria):
        if memoria[i] == '-':
            if count == 0:
                endereco_livre = i
            count += 1
            if count == tamanho_processo:
                for j in range(endereco_livre, endereco_livre + tamanho_processo):
                    memoria[j] = id_processo
                print("Processo iserido com sucesso!")
                return memoria
        else:
            count = 0
        
        #print(f"Endereco livre: {endereco_livre}")
        #print(f"Count: {count}")
        #print(f"Tamanho processo: {tamanho_processo}")

    print("Memory Overflow!")
    return memoria
            
    # conta todos '-' depois até count == tamanho_processo
    # se memoria[i] != '-' e count < tamanho_processo reinicia count
    # se chegar ao fim do for exit com false

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

def run_particao_fixa(tam_memoria, fila_de_entrada):
    # Inicializa a memoria
    memoria = []
    for i in range(0,tam_memoria):
        memoria.append('-')
    # Roda fila de entrada
    imprime_status_memoria(memoria, tam_memoria)
    for i in fila_de_entrada:
        
        # Insere ou remove da memoria
        if i[0] == "IN":
            memoria = insere_na_memoria(memoria, tam_memoria, i[1], int(i[2]))

        elif i[0] == "OUT":
            memoria = remove_da_memoria(memoria, tam_memoria, i[1])

        imprime_status_memoria(memoria, tam_memoria)
    # Imprime status da memoria   
    