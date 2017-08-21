# Stack을 구현하다
class Stack(list):
    # Python의 기본 클래스인 list를 상속받는다
    
    # push
    push = list.append
    # 상속받은 list를 사용하기에 method로 정의 불필요.
    
    # pop은 구현하지 않는다. list에 pop()이 이미 있기 때문에 불필요.
    
    def peek(self):
        return self[-1]
    
    def empty(self):
        if not self:
            return True
        return False   

# Test Code for Stack
if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.push(10)
    
    while not s.empty():
        print(s.pop(), end = ' ')