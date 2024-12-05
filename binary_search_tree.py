class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            def insert_to_vertex(data, vertex):
                if data < vertex.data:
                    if vertex.left:
                        insert_to_vertex(data, vertex.left)
                    else:
                        vertex.left = Node(data)
                else:
                    if vertex.right:
                        insert_to_vertex(data, vertex.right)
                    else:
                        vertex.right = Node(data)
            insert_to_vertex(data, self.root)

    def display(self):
        result = ""

        def vrl(result, vertex):
            if vertex:
                if vertex.data:
                    result += str(vertex.data) + " "
                vrl(result, vertex.left)
                vrl(result, vertex.right)
            return result
        print(vrl(result, self.root))


tree = BST()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(8)
tree.insert(7)
tree.insert(99)

tree.display()
