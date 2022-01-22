class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def addFront(self, value):
        node1 = Node(value)
        node1.next = self.head
        self.head = node1
    def removeNode(self):
        if self.head == None:
            return None
        self.head = self.head.next
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.value
    def printSLL(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next

l_list1 = SLL()
l_list1.addFront(3)
l_list1.addFront(5)
l_list1.addFront(7)

l_list1.printSLL()
l_list1.removeNode()
l_list1.printSLL()
l_list1.removeNode()
l_list1.removeNode()
print(l_list1.front())