import os 
import ParticaoFixa as PF

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

def main(): 

    print("*************************************************************************")
    print("***********************COMECOU DENOVO ESSE DIABO*************************")
    print("*************************************************************************")

    while(1):
        #clear_terminal()
        # Cria fila de entradas
        fila_de_entrada = []

        # Pergunta o nome do arquivo
        #clear_terminal()
        nome_arquivo = input("Informe o nome do arquivo:\n> ")

        # Abre o arquivo e carrega na fila de entrada
        #clear_terminal()
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                fila_de_entrada.append(linha.replace(",","").replace("("," ").replace(")", "").split())
                print(fila_de_entrada)

        # Pergunta o tipo de particionamento
        tipo_particionamento = -1
        while(tipo_particionamento != 1 and tipo_particionamento != 2 and tipo_particionamento != 3):
            #clear_terminal()
            tipo_particionamento = int(input("Informe o tipo de particionamento:\n[1] Particao Fixa\n[2] Particao Variavel\n[3] Particao Buddy\n> "))
         
        # Pergunta o tamanho da memoria
        tamanho_memoria = -1
        while (1):
            #clear_terminal()
            tamanho_memoria = int(input("Informe o tamanho da memoria:\n> "))
            if potencia_de_dois(tamanho_memoria) == False:
                input("Tamanho da memoria deve ser potencia de dois!\n\nPressione enter para continuar...")
            else:
                #clear_terminal()
                break
        
        # Chama o tipo de particionamento
        if tipo_particionamento == 1:
            PF.run_particao_fixa(tamanho_memoria, fila_de_entrada)
        elif tipo_particionamento == 2:
            pass
        elif tipo_particionamento == 3:
            pass
        
        restart_flag = -1
        while(restart_flag != 0 and restart_flag != 1):
            restart_flag = int(input("Deseja reiniciar o programa?\n[1] Sim\n[0] Não\n> "))
            #clear_terminal()
        
        if restart_flag == 0:
           exit()
        
if __name__ == "__main__":
    main()