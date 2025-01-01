#przechodzenie wzdłużne: VLR;
#V - vertex L - left, R - Right
#3 - 2 - 1 - 8 - 7 - 99


#przechodzeie poprzeczne : LVR;
#1 - 2 - 3 - 3 - 7 - 8 - 99

#przechodzenie wstecznel: LRV;
#1 - 2 - 7 - 99 - 8 - 3

class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
        else:
            def insert_to_vertex(data, vertex):
                if data < vertex.data:
                    if vertex.left == None:
                        vertex.left = Node(data)
                    else:
                        insert_to_vertex(data, vertex.left)
                if data > vertex.data:
                    if vertex.right == None:
                        vertex.right = Node(data)
                    else:
                        insert_to_vertex(data, vertex.right)

            insert_to_vertex(data, self.root)

    def display(self):
        result = ""

        def vlr(result, vertex):
            if vertex:
                if vertex.data:
                    result += str(vertex.data) + "-"
                    result = vlr(result, vertex.left)
                    result = vlr(result, vertex.right)
            return result

        def lvr(result, vertex):
            if vertex:
                if vertex.data:
                    result =str(result, vertex.left) + result
                    result += str(result, )


        print(vlr(result, self.root))


tree = BST()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(7)
tree.insert(99)

tree.display()




