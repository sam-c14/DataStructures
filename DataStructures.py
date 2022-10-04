class Stack:
    def __init__(self):
        self.__newStack=[]
    def push(self,value):
        self.__newStack.append(value)
    def pop(self):
        return self.__newStack.pop()
    def peek(self):
        return self.__newStack[self.__newStack.__len__()-1]if self.__newStack.__len__()-1 > 0 else False
    def getStack(self):
        return self.__newStack
    def isEmpty(self):
        return True if len(self.__newStack) == 0 else False

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
        return True
    def dequeue(self):
        first_item=self.queue[0]
        if self.queue.__len__() > 0:
            self.queue.remove(first_item)
            return first_item
        else: return False     
    def peek(self):
        return self.queue[0] if self.queue.__len__() > 0 else False
    def isEmpty(self):
        return True if self.queue.__len__() ==0 else False
    def getQueue(self):
        return self.queue


class BinaryNode:
    def __init__(self,value,leftChild=None,rightChild=None):
        self.value=value
        self.leftChild=leftChild
        self.rightChild=rightChild
    

class LinkedNode:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def isEmpty(self):
        return self.__head == None
    def push(self,value):
        self.__head=LinkedNode(value,self.__head)
        if self.__tail == None:self.__tail = self.__head
    def append(self,value):
        if self.isEmpty():
            self.push(value)
            return
        self.__tail.next=LinkedNode(value)
        self.__tail=self.__tail.next
    def node_at(self,index):
        if index < 0 or index > self.list_len(): return None
        current_node=self.__head
        current_index=0
        while current_node != None and current_index < index:
            current_node=current_node.next
            current_index +=1
        return current_node
    def insert_after(self,node,value):
        if node == self.__tail:
            self.append(value)
            return self.__tail
        node.next=LinkedNode(value,node.next)
        return node.next
    def print_list(self):
        list_arr=[]
        current_node=self.__head
        while current_node != None:
            list_arr.append(current_node.value)
            current_node=current_node.next
        return list_arr
    def pop(self):
        value=self.__head.value
        self.__head=self.__head.next
        if self.__head == None:self.__tail=None
        return value
    def remove_last(self):
        if self.__head == None : return
        if self.__head.next == None :
            self.pop()
            return
        current_node=self.__head
        while current_node.next != self.__tail:
            current_node=current_node.next
        value=current_node.next.value
        self.__tail=current_node
        self.__tail.next=None
        return value
    def remove_after(self,node):
        value=node.next.value
        if node.next == self.__tail : self.__tail=node
        node.next=node.next.next
        return value
    def get_tail(self):
        return self.__tail
    def print_reverse(self):
        stack=Stack()
        current_node=self.__head
        while current_node != None:
            stack.push(current_node.value)
            current_node=current_node.next
        while not stack.isEmpty() :
            print(stack.pop())
    def list_len(self):
        current_node=self.__head
        length=0
        if self.__head == None : return length
        while current_node != None:
            length +=1
            current_node =current_node.next
        return length
    def middle_node(self):
        middle_index=self.list_len() // 2
        current_index=0
        current_node=self.__head
        if self.__head == None : return None
        while current_index < middle_index :
            current_index +=1
            current_node=current_node.next
        return current_node

        # Uses index of last_node in the list to access last node and takes out nodes from the list
        # Then recursively calls the function with each valid next pointer pointing to each node in reverse order by returning current_node when its not None
        # When current_node is None recursion ends
    def __reverse(self,current_node=''):
        last_node_index=self.list_len() - 1
        if current_node == ''  : current_node =self.__tail
        else : current_node=self.node_at(last_node_index)
        self.remove_last()
        if  current_node == None : return
        current_node.next=self.__reverse(current_node)
        return current_node
    def reverse_list(self):
        self.__head = self.__reverse()
        return self.__head

    # At first call current_node is set to head node and loop loops till node with value != value is found at every call of the function
    # This helps incase first 3 or more node have value == value they are easily removed
    # Checks if current nodes next value is == value -> True : set current node.next to value after it and call 
    # Call other function if recursion was not performed in if statement
    # recursion end when current node is None
    def __filter(self,value,current_node):
        if current_node == '':current_node=self.__head
        recursion_done=False
        while current_node != None :
            if current_node.value == value: current_node=current_node.next
            else : break
        if current_node == None : return 
        if current_node.next != None and current_node.next.value == value:
            current_node.next = current_node.next.next
            current_node.next=self.__filter(value,current_node.next)
            recursion_done=True
        if not recursion_done : current_node.next= self.__filter(value,current_node.next)
        return current_node
    def filter_list(self,value):
        self.__head=self.__filter(value,'')
        return self.__head

class Heap:
    def __init__(self,priority,new_list=[]):
        self.__priority=priority.lower()
        if new_list != [] : self.__heapify(new_list)
        else :
            self.__list=new_list
    def __left_child_index(self,parent):
        return 2 * parent + 1
    def __right_child_index(self,parent):
        return 2 * parent + 2
    def __swap_values(self,first_index,second_index):
        [self.__list[first_index],self.__list[second_index]] = [self.__list[second_index],self.__list[first_index]]
    def __parent_index(self,child_index):
        return (child_index - 1) // 2
    def __first_has_higher_priority(self,first_value,second_value):
        if self.__priority == 'max' : 
            return first_value > second_value
        return first_value < second_value
    def __has_higher_priority(self,first_index,second_index):
        if first_index >= len(self.__list): return second_index
        first_value=self.__list[first_index] 
        second_value=self.__list[second_index] 
        is_first=self.__first_has_higher_priority(first_value,second_value)
        return first_index if is_first else second_index
    def insert(self,value):
        self.__list.append(value)
        self.__sift_up(len(self.__list) - 1)
    def __sift_up(self,index):
        parent_index=self.__parent_index(index)
        child_index=index
        while child_index > 0 and child_index == self.__has_higher_priority(child_index,parent_index):
            self.__swap_values(child_index,parent_index)
            child_index=parent_index
            parent_index=self.__parent_index(child_index)
    def print_heap(self):
        return self.__list
    def remove(self):
        self.__swap_values(0,len(self.__list)-1)
        self.__list.pop()
        self.__sift_down(0)
    def __sift_down(self,index):
        if index < 0 or index >= len(self.__list):return -1
        parent_index=index
        left_child=self.__left_child_index(parent_index)
        right_child=self.__right_child_index(parent_index)
        while True :
            current_index=parent_index
            if left_child == self.__has_higher_priority(left_child,current_index):
                current_index=left_child
            if right_child == self.__has_higher_priority(right_child,current_index):
                current_index=right_child
            if current_index == parent_index:return 
            self.__swap_values(current_index,parent_index)
            parent_index=current_index
            left_child=self.__left_child_index(parent_index)
            right_child=self.__right_child_index(parent_index)
    def remove_at(self,index):
        current_index=index
        last_index=len(self.__list) - 1
        if current_index == last_index : return self.__list.pop()
        self.__swap_values(current_index,last_index)
        self.__list.pop()
        self.__sift_up(current_index)
        self.__sift_down(current_index)

    def index_of(self,value,current_index=0):
        if current_index > len(self.__list) or self.__first_has_higher_priority(value,self.__list[current_index] ):return -1
        left_child=self.__left_child_index(current_index)
        right_child=self.__right_child_index(current_index)
        if value == self.__list[current_index] : return current_index
        if left_child < len(self.__list) and value == self.__list[left_child] : return left_child
        if right_child < len(self.__list) and value == self.__list[right_child] : return right_child
        left = self.index_of(value,left_child)
        if left != -1 :return left
        return self.index_of(value,right_child)
    
    def __heapify(self,list):
        middle_index =len(list) // 2 -1
        self.__list=list

        while middle_index >= 0 :
            self.__sift_down(middle_index)
            middle_index -=1