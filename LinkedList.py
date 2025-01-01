class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class List():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        appened_node = Node(data)
        if self.head.data is None:
            self.head = appened_node
        else:
            counter = self.head
            while counter.next is not None:
                counter = counter.next
            counter.next = appened_node
    def dispaly(self):
        counter = self.head
        print(counter.data)
        while counter.next is not None:
            print(counter.next.data)
            counter = counter.next

    def length(self):
        counter = self.head
        if self.head.data is None:
            return 0
        output = 1
        while counter.next is not None:
            output+=1
            counter = counter.next
        return output
    def drop(self,i):
        if self.head is None or self.head.data is None:
            print("Lista jest pusta")
            return
        if i>= self.length() or i <0:
            print("Zły indeks")
            return
        if i==0:
            self.head = self.head.next
            return
        counter = self.head
        position = 0
        while counter.next is not None:
            former = counter
            counter = counter.next
            if position+1 == i:
                former.next = counter.next
                return
            position+=1

    def drop_duplicates(self):
        counter = self.head
        former = None
        duplicates = {}
        while counter:
            if counter.data in duplicates:
                former.next = counter.next
            else:
                duplicates[counter.data] = 'co?'
                former = counter
            counter = counter.next
    def acquire(self, x):
        if self.head.data is None:
            print('Lista jest pusta')
            return
        if  x>= self.length() or x < 0:
            print("Zły indeks")
            return
        counter = self.head
        position = 0
        while counter:
            if  position is x:
                return counter.data
            position += 1
            counter = counter.next


    def reverse_itter(self):
        former = None
        counter = self.head
        while counter:
            consequent = counter.next
            counter.next = former
            former = counter
            counter = consequent
        self.head = former

    def reverse_recur(self):
        def reverse_recur_inner(counter, former):
            if not counter:
                self.head  = former
                return
            consequent = counter.next
            counter.next = former
            reverse_recur_inner(consequent, counter)
        reverse_recur_inner(counter=self.head, former=None)


lista = List()
lista.append(4)
lista.append(11)
lista.append(4)
lista.append(7)
lista.append(4)
lista.append(8)
lista2= List()
lista3 = List()


for i in range(10):
    lista3.append(i)

print(lista.length())
print(lista2.length())
print(lista3.length())

print("Lista 3 przed usunięciem elementu: ")
print(lista3.dispaly())

lista3.drop(7)

print("Lista 3 po usunięciem elementu: ")
print(lista3.dispaly())

lista3.drop(100)
lista.drop(-9)
lista2.drop(4)

print("Lista przed odwróceniem: ")
print(lista.dispaly())
print("Lista po odwróceniu")
lista.reverse_itter()
print(lista.dispaly())
print("Lista po odwróceniu:")
lista3.reverse_recur()
print(lista3.dispaly())

print("Lista z duplikatami: ")
print(lista.dispaly())
print("Lista bez duplikatów")
lista.drop_duplicates()
print(lista.dispaly())

print("Pojedyncze elementy listy")
print(lista.acquire(3))
print(lista2.acquire(0))
print(lista3.acquire(1))