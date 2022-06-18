# cria a memória inicial (preenche a memória com 0)
def cria_memoria(tam_memoria):
    return [0 for i in range(tam_memoria)]


# devolve uma lista com duas listas
def particiona_memoria(memoria):
    return list((memoria[i::2] for i in range(2)))

# retorna verdadeiro ou falso se o bloco de memória está desocupado (todo preenchido com 0)


def checa_memoria_vazia(memoria):
    return memoria.count(memoria[0] == len(memoria))


def insere_na_memoria(memoria, id_processo, tamanho_processo):

    # ATENÇÃO: aqui deve conferir se é cada bloco de memória ou toda a memória
    if len(memoria) >= tamanho_processo and len(memoria) > 0:
        memoria_particionada = particiona_memoria(memoria)

        for memoria in memoria_particionada:
            # checa se memoria é vazia (ou seja, todos os elementos = 0)
            if(checa_memoria_vazia(memoria)):
                # se sim, preenche o bloco de memoria
                for i in range(0, tamanho_processo):
                    memoria[i] = id_processo

    return memoria


def run_buddy(tam_memoria, fila_entrada):
    # preenche memória
    memoria = cria_memoria(tam_memoria)

    for i in fila_entrada:
        # Insere ou remove da memoria
        if i[0] == "IN":
            tam_processo = int(i[2])
            nome_processo = i[1]

            memoria = insere_na_memoria(memoria, nome_processo, tam_processo)
            pass
        elif i[0] == "OUT":
            pass


memoria = [0 for i in range(4)]

memoria_particionada = particiona_memoria(memoria, 3)
for mem in memoria_particionada:
    print(mem)
