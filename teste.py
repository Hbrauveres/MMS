class Node:
   def __init__(self, size):
      self.process = None
      self.size = size
      self.frag = 0
      self.livre = True
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
        new_node1 = Node(new_size)
        new_node2 = Node(new_size)
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

    def join_buddy():
        pass


mem = Memory(128)
mem.try_insert(1,"d")
mem.try_insert(25,"a")
mem.try_insert(32,"b")
mem.try_insert(16,"c")
mem.try_insert(16,"e")
mem.try_insert(5,"f")
mem.try_insert(5,"g")
mem.try_insert(54,"h")
mem.print_memory()
