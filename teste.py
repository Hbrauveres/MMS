class Node:
   def __init__(self, size, parent=None):
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
                print(f"Tamanho do nodo > Tamanho Processo")
                if node.livre:
                    print(f"Nodo Livre")
                    if node.size/2 >= proc_size:
                        print(f"Tamanho do nodo/2 >= Tamanho Processo")
                        print(f"Criando Buddy Nodes")
                        self.create_buddy(node)
                        self.print_memory()
                        node = self.head
                        input()
                    else:
                        print(f"Tamanho do nodo/2 < Tamanho Processo")
                        print(f"Inserindo Processo")
                        self.insere_processo(node,proc_id,proc_size)
                        self.print_memory()
                        print(f"Processo Inserido")
                        finished = True
                        # node.livre = False
                        # node.process = proc_id
                else:
                    print(f"Nodo Ocupado")
                    if node.next is not None:
                        print(f"Pegando Proximo Nodo")
                        node = node.next
                        print(f"Proximo nodo adquirido")
                    else:
                        print("Não há mais nodos")
                        print("Finalizando")
                        finished = True
            else:
                print(f"Tamanho do nodo < Tamanho Processo")
                if node.next is not None:
                    print(f"Pegando Proximo Nodo")
                    node = node.next
                    print(f"Proximo nodo adquirido")
                else:
                    print("Não há mais nodos")
                    print("Finalizando")
                    finished = True

    def create_buddy(self, node):
        new_size = node.size/2
        print(f"new size = {new_size}")
        new_node1 = Node(new_size,node)
        new_node2 = Node(new_size,node)
        new_node1.next = new_node2
        new_node2.next = node.next
        new_node2.prev = new_node1
        new_node1.prev = node.prev
        
        if node.next is not None:
            print(f"proximo nodo vale: {node.next.size}")
            node.next.prev = new_node2

        if node.prev is not None:
            print(f"nodo anterior vale: {node.prev.size}")
            node.prev.next = new_node1

        if new_node1.prev == None:
            print(f"NEW HEAD! HEAD VALUE = {new_node1.size}")
            self.head = new_node1

    def insere_processo(self, node, proc_id,proc_size):
        node.livre = False
        node.frag = node.size - proc_size
        node.process = proc_id

    def print_memory(self):
        node = self.head
        while node is not None:
            print(node.livre, node.process, node.size)
            #if node.prev == None:
            #    print("None", end =" ")
            #else:
            #    print(node.prev.size, end =" ")
            #print(node.size, end = " ")
            #if node.next == None:
            #    print("None")
            #else:
            #    print(node.next.size)
            
            node = node.next

    def get_buddy_node(self,node):
        pass

    def buddy_clean(self):
        # TERMINAR BUDDY CLEAN!!!!
        pass
    
        '''node = self.head
        finished = False
        while not finished:
            if node.livre:
                if node.next is not None:
                    aux_node = node.next
                    node_par = None
                    while aux_node is not None:
                        if node.parent == aux_node.parent:
                            if aux_node.livre:
                                node_par = aux_node
                                break
                    
                    node.parent.prev = node.prev
                    node.parent.next = node_par.next
                    
                    if node.prev is not None:
                        node.prev.next = node.parent
            

            else:
                node = node.next'''
                                    

    def remove_processo(self, id_processo):
        node = self.head
        finished = False
        while not finished and node is not None:
            if node.process == id_processo:
                node.livre = True
                node.process = None
                node.frag = 0
                finished = True
                self.buddy_clean()
            node = node.next
        
        if finished == False:
            print(f"Processo {id_processo} não encontrado")
   

mem = Memory(128)
mem.try_insert(1,"d")
mem.try_insert(25,"a")
mem.try_insert(32,"b")
mem.try_insert(16,"c")
mem.try_insert(16,"e")
mem.try_insert(5,"f")
mem.try_insert(5,"g")
mem.try_insert(54,"h")
mem.remove_processo("z")
mem.print_memory()
