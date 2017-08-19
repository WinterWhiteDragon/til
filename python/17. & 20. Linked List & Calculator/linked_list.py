class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        self.before = None
        self.current = None
        
        self.num_data = 0
    
    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False
    
    def size(self):
        return self.num_data
    
    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.num_data += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.num_data += 1
    
    def traverse(self, mode = 'next'):
        if self.empty():
            return None
        
        if mode == 'first':
            self.before = self.head
            self.current = self.head
        else:
            if self.current.next == None:
                return None
            self.before = self.current
            self.current = self.current.next
            
        return self.current.data
    
    def remove(self):
        ret_data = self.current.data
        
        if self.num_data == 1:
            self.head = None
            self.tail = None
            self.before = None
            self.current = None        
        elif self.current == self.head:
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next
        else:
            if self.current == self.tail:
                self.tail = self.before
            self.before.next = self.current.next
            self.current = self.before
        
        self.num_data -= 1
        return ret_data

def show_list(slist):
    data = slist.traverse('first')

    if data:
        print(data, end = '  ')
        # 처음으로 traverse하기 전, 시작점에 data가 있을 가능성에 대응하기 위해 먼저 print하고 traverse하고 while 반복문을 실행한다.
        data = slist.traverse()
        while data:
            print(data, end = '  ')
            data = slist.traverse()
    else:
        print("There is no data")