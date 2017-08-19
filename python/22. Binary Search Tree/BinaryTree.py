class TreeNode:
    def __init__(self):
        self._data = None
        self.left = None
            # node's left child node
        self.right = None
            # node's right child node
    
    def __del__(self):
        print('TreeNode of {} is deleted!'.format(self._data))
    
    @property
        # property만 하면 getter다
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    
    def set_root(self, r):
        self.root = r
        
    def make_node(self):
        return TreeNode()
    
    def get_node_data(self, cur):
        return cur.data
    
    def set_node_data(self, cur, data):
        # get이 있으면 set이 있어야 한다
        cur.data = data
        
    def get_left_sub_tree(self, cur):
        return cur.left
    
    def get_right_sub_tree(self, cur):
        return cur.right
    
    def make_left_sub_tree(self, cur, left):
        cur.left = left
    
    def make_right_sub_tree(self, cur, right):
        cur.right = right
        
    def preorder_traverse(self, cur, func):
        # 탈출 조건
        if not cur:
            return
        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)
    
    def inorder_traverse(self, cur, func):
        if not cur:
            return
        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)
    
    def postorder_traverse(self, cur, func):
        if not cur:
            return
        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)



if __name__ == "__main__":
    bt = BinaryTree()
    n1 = bt.make_node()
    bt.set_node_data(n1, 1)
    n2 = bt.make_node()
    bt.set_node_data(n2, 2)
    n3 = bt.make_node()
    bt.set_node_data(n3, 3)
    n4 = bt.make_node()
    bt.set_node_data(n4, 4)
    n5 = bt.make_node()
    bt.set_node_data(n5, 5)
    n6 = bt.make_node()
    bt.set_node_data(n6, 6)
    n7 = bt.make_node()
    bt.set_node_data(n7, 7)
    
    bt.set_root(n1)
    bt.make_left_sub_tree(n1, n2)
    bt.make_right_sub_tree(n1, n3)
    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)
    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)
    
    f = lambda x: print(x, end = "  ")
    bt.preorder_traverse(bt.get_root(), f)