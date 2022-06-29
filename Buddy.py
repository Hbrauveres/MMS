class Node:

    __Node_id = 0

    def __init__(self, size, parent=None):
        self.Node_id = Node.__Node_id
        Node.__Node_id += 1
        self.process = None
        self.size = size
        self.frag = 0
        self.livre = True
        self.parent = parent
        self.next = None
        self.prev = None

class Memory:
    def __init__(self, size):
        self.head = Node(size)

    def try_insert(self,proc_size,proc_id):
        finished = False
        node = self.head
        while(not finished):
            if node.size >= proc_size:
                #print(f"Tamanho do nodo > Tamanho Processo")
                if node.livre:
                    #print(f"Nodo Livre")
                    if node.size/2 >= proc_size:
                        #print(f"Tamanho do nodo/2 >= Tamanho Processo")
                        #print(f"Criando Buddy Nodes")
                        self.create_buddy(node)
                        #self.print_memory()
                        node = self.head
                        #input()
                    else:
                        #print(f"Tamanho do nodo/2 < Tamanho Processo")
                        #print(f"Inserindo Processo")
                        self.insere_processo(node,proc_id,proc_size)
                        #self.print_memory()
                        print(f"Processo {proc_id} Inserido")
                        finished = True
                        # node.livre = False
                        # node.process = proc_id
                else:
                    #print(f"Nodo Ocupado")
                    if node.next is not None:
                        #print(f"Pegando Proximo Nodo")
                        node = node.next
                        #print(f"Proximo nodo adquirido")
                    else:
                        print(f"Memory Overflow! Processo {proc_id} não inserido.")
                        #print("Finalizando")
                        finished = True
            else:
                #print(f"Tamanho do nodo < Tamanho Processo")
                if node.next is not None:
                    #print(f"Pegando Proximo Nodo")
                    node = node.next
                    #print(f"Proximo nodo adquirido")
                else:
                    print(f"Memory Overflow! Processo {proc_id} não inserido.")
                    #print("Finalizando")
                    finished = True

    def create_buddy(self, node):
        new_size = node.size/2
        #print(f"new size = {new_size}")
        new_node1 = Node(new_size,node)
        new_node2 = Node(new_size,node)
        new_node1.next = new_node2
        new_node2.next = node.next
        new_node2.prev = new_node1
        new_node1.prev = node.prev
        
        if node.next is not None:
            #print(f"proximo nodo vale: {node.next.size}")
            node.next.prev = new_node2

        if node.prev is not None:
            #print(f"nodo anterior vale: {node.prev.size}")
            node.prev.next = new_node1

        if new_node1.prev == None:
            #print(f"NEW HEAD! HEAD VALUE = {new_node1.size}")
            self.head = new_node1

    def insere_processo(self, node, proc_id,proc_size):
        node.livre = False
        node.frag = node.size - proc_size
        node.process = proc_id
        #self.print_memory()

    def print_memory(self):
        node = self.head
        output = []
        frag_total = 0
        while node is not None:
            if node.livre:
                output.append(node.size)
            else:
                frag_total += node.frag
            node = node.next
        print("Fragmentacao Interna Total:",frag_total)
        print(output)
        #while node is not None:
        #    print(node.livre, node.process, node.size)
        #    node = node.next
        #input()

    def buddy_join(self):
        #print("INICIANDO BUDDY JOIN")
        while(1):
            nodos_livres = []
            nodos_livres_print = []
            iter_nodo = self.head
            while iter_nodo is not None:
                #print("Procurando nodo livre")
                if iter_nodo.livre:
                    #print(f"Nodo livre {iter_nodo.size} encontrado")
                    nodos_livres.append(iter_nodo)
                    nodos_livres_print.append(iter_nodo.Node_id)
                iter_nodo = iter_nodo.next
            
            nodos_pares = []
            nodos_pares_print = []
            iter_lista = [x for x in nodos_livres]
            #print(f"ITER LISTA = {[x.Node_id for x in iter_lista]}")
            iter_nodo = self.head
            
            for nodo in iter_lista:
                if nodo.next is not None:
                    if nodo.next.parent == nodo.parent and nodo.next.livre:
                        #print(f"Nodo par {nodo.next.Node_id} encontrado")
                        nodos_pares.append(nodo.next)
                        nodos_pares_print.append(nodo.next.Node_id)
                    else:
                        #print(f"Nodo {nodo.Node_id} par não encontrado")
                        nodos_livres_print.remove(nodo.Node_id)
                        nodos_livres.remove(nodo)
                else:
                    nodos_livres_print.remove(nodo.Node_id)
                    nodos_livres.remove(nodo)
            
            if nodos_pares == []:
                break

            #print(f"Nodos livres: {nodos_livres_print}")
            #print(f"Nodos pares: {nodos_pares_print}")
           
            #print("Juntando buddies")
            for i in range(0,len(nodos_livres)):
                
                nodo_livre = nodos_livres[i]
                nodo_par = nodos_pares[i]
                #print(f"Juntando nodo {nodo_livre.Node_id} com seu par {nodo_par.Node_id}")

                nodo_pai = nodo_livre.parent

                nodo_pai.prev = nodo_livre.prev
                if nodo_livre.prev is not None:
                    nodo_livre.prev.next = nodo_pai
                    
                nodo_pai.next = nodo_par.next
                if nodo_par.next is not None:
                    nodo_par.next.prev = nodo_pai

                if nodo_livre == self.head:
                    self.head = nodo_pai
                #print("Buddies juntados")
                #self.print_memory()         

    def remove_processo(self, id_processo):
        node = self.head
        finished = False
        while not finished and node is not None:
            if node.process == id_processo:
                node.livre = True
                node.process = None
                node.frag = 0
                finished = True
                self.buddy_join()
                #self.print_memory()
                print(f"Processo {id_processo} removido!")
                break
            node = node.next
        
        if finished == False:
            print(f"Processo {id_processo} não encontrado")
   

def run_buddy_system(tam_memoria,fila_de_entrada):
    mem = Memory(tam_memoria)
    for i in fila_de_entrada:

        # Insere ou remove da memoria
        if i[0] == "IN":
            mem.try_insert(int(i[2]),i[1])

        elif i[0] == "OUT":
            mem.remove_processo(i[1])
        
        mem.print_memory()
