from DataStructures import BinaryNode, LinkedList, Queue, Stack,Heap

myStack=Stack()

def isBalanced(string):
    for item in string:
        if item == '(':
            myStack.push(item)
        elif item == ')':
            if(myStack.isEmpty()):  return False
            else:myStack.pop()
    return True if myStack.isEmpty() else False

# print(isBalanced('h((e))llo(world)()'))


class BinaryTree:
    def __init__(self):
        self.__binary_list=[]
        self.__node=''
    def newTree(self):
        node1=BinaryNode(15)
        node2=BinaryNode(10)
        node3=BinaryNode(25)
        node4=BinaryNode(5)
        node5=BinaryNode(12)
        node6=BinaryNode(17)

        node1.leftChild=node2
        node1.rightChild=node3
        node2.leftChild=node4
        node2.rightChild=node5
        node3.leftChild=node6
        self.node=node1
        return self.node
    
    def pre_order(self,node=''):
        if(node == ''):
            node =self.newTree()
        self.tree_to_list(node.value) if node else self.tree_to_list(None)
        node and self.pre_order(node.leftChild)
        node and self.pre_order(node.rightChild)

    def tree_to_list(self,value):
        self.__binary_list.append(value)

    def serialize(self):
        self.pre_order()
        return self.__binary_list

    def list_to_tree_left(self,node):
      node.leftChild=BinaryNode(self.check_value())
      self.__binary_list.remove(self.check_value())
      self.deserialize(node.leftChild)

    def list_to_tree_right(self,node,):
            node.rightChild=BinaryNode(self.check_value())
            self.__binary_list.remove(self.check_value())
            self.deserialize(node.rightChild)

# At the last value list becomes empty so the value returns an access error
# Returns None value so that the other right function is not called 
    def check_value(self,condition=1):
        value=self.__binary_list[0] if self.__binary_list.__len__() > 0 else ''
        if condition == 0:
            return ''
        elif value == None:
            self.__binary_list.remove(value)
            return value
        return value

# Using recursion call a function each time to return the first value of the list
# Didn't use the and operator here because logical ops are binary
# The logic here is that None values are always going to be removed by the check_value function and the other remove is just a byPass 
    def deserialize(self,node=''):
        if self.__node == '' and self.__binary_list[0] != None:
            self.__node=BinaryNode(self.__binary_list[0])
            self.__binary_list.remove(self.__binary_list[0])
            self.deserialize(self.__node)
        if self.__binary_list.__len__() > 0:
           self.check_value() and self.list_to_tree_left(node)
           self.check_value() and self.list_to_tree_right(node)

    def get_new_tree(self):
        return self.__node

new_tree=BinaryTree()
print(new_tree.serialize())
new_tree.deserialize()
print(new_tree.get_new_tree().value)




