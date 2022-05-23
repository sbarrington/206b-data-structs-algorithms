from random import randint

class Node:
    def __init__(self, data, left=None, right=None):      
        self.data = data
        self.left = left
        self.right = right
   
    
class BST:
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, None, data)

    # BASE HELPERS (PRE-PROVIDED):
    def insert_helper(self, current, parent, data):
        if current == None:
            if data < parent.data:
                parent.left = Node(data)
            else:
                parent.right = Node(data)
        elif data < current.data:
            self.insert_helper(current.left, current, data)
        elif data > current.data:
            self.insert_helper(current.right, current, data)
        else:
            return
        
    def inorder_traversal(self):
        self.inorder_traversal_helper(self.root)
    
    def inorder_traversal_helper(self, root):
        if root == None:
            return
        self.inorder_traversal_helper(root.left)
        print (root.data)
        self.inorder_traversal_helper(root.right)
        
    def preorder_traversal(self):
        self.preorder_traversal_helper(self.root)
    
    def preorder_traversal_helper(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder_traversal_helper(root.left)
        self.preorder_traversal_helper(root.right)
        
    # ASSIGNMENT HELPERS (WRITTEN):
    def delete(self, data):
        self.delete_helper(self.root, None, data)
    def delete_helper(self, current, parent, data):
        if current == None:
            return # element not in tree

        if current.data == data:
            if current.left == None and current.right == None:
                self.delete_leaf(current, parent)
            elif current.left == None or current.right == None:
                self.delete_node_with_one_child(current, parent)
            else: # node has two children
                self.delete_node_with_two_children(current, parent)
               
        if data < current.data:
            self.delete_helper(current.left, current, data)
        else: 
            self.delete_helper(current.right, current, data)
                
    def delete_leaf(self, current, parent):
        if parent == None: # special case: deleting root
            self.root = None
            return
        if current.data < parent.data:
            parent.left = None
        else:
            parent.right = None
            
    def delete_node_with_one_child(self, current, parent):
        if parent == None:   # special case: current is self.root
            if current.left == None:
                self.root = current.right
            elif current.right == None:
                self.root = current.left
             
        elif current.data < parent.data:
            if current.left != None:
                parent.left = current.left
            else:
                parent.left = current.right
        else: # current.data > parent.data
            if current.left != None:
                parent.right = current.left
            else:
                parent.right = current.right
                
    def findsuccessor(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node
    
    def delete_node_with_two_children(self, current, parent):
        # If node not in tree, raise error 
        if current.right == None:
            return "Error: node not in tree"
        # If current node doesn't have 2 children, or doesnt exist, return error
        if (current.left == None or current.right == None):
            return "Error: node does not have 2 children"
        
        print(f'Deleting node: {current.data}')
        # Shift to the next node to the right 
        print(f'Parent before reset: {parent.data}')
        node_to_delete = current # Node we're deleting
        print(f'Parent after reset: {node_to_delete.data}')
        parent = current
        current = current.right
        print(f'New current node: {current.data}') 
        # Traverse down left side only to obtain next lowest value
        while current.left != None: 
            parent = current
            current = current.left 
            print(f'New current: {current.data}')
            
        # Update the node to be deleted with the next_lowest_value
        node_to_delete.data = current.data
        print(f'The value of current, and thus the node I am trying to delete, is: {current.data}')
        # Delete lowest value node 
        if current.right != None:
            self.delete_node_with_one_child(current, parent)
        else:
            self.delete_leaf(current, parent)
        print(f'parent.data is now: {node_to_delete.data}')
        
        return

    def delete_bst(self, root):
        # Traverse the left first
        if root.left != None:
            print(f'Triggering function to the left for {root.left.data}')
            self.delete_bst(root.left)
        # Then traverse the right 
        if root.right != None:
            print(f'Triggering function to the right for {root.right.data}')
            self.delete_bst(root.right)
        # Base case: if you reach the end of the tree 
        if root == None:
            return 
        # Check the current node's left child
        if root.left != None:
            current = root.left
            print(f"The root node we're at is: {root.data}")
            print(f"The 'current' node (aka left child of root) is: {current.data}")
            # Check if the node's left child also has children 
            if current.left != None:
                print(f"The 'current' node's left child is: {current.left.data}")
            # Remove the left child if it doesn't have it's own children 
            if (current.left == None and current.right == None):
                print(f"deleting {current.data} as it has no kids")
                self.delete_leaf(current, root)
        # Check current nodes right child
        if root.right != None: 
            current = root.right
            print(f"The root node we're at is: {root.data}")
            print(f"The 'current' node (aka right child of root) is: {current.data}")
            # Check if the node's right child also has children 
            if current.right != None:
                print(f"The 'current' node's right child is: {current.right.data}")
            # Remove the right child if it doesnt have it's own children 
            if (current.left == None and current.right == None):
                print(f"deleting {current.data} as it has no kids")
                self.delete_leaf(current, root)
        print(f'Current root value: {root.data}')
        
        # Special case for the original root node at the end  
        if (root.left == None and root.right == None):
            print(f'Special case activated for {root.data}')
            self.delete_leaf(root, None) 


def generate_nodes(n, bst):
    for i in range(0, n):
        bst.insert(randint(0, 1000))
    # Traverse in order to check creation   
    #bst.inorder_traversal()
    bst.preorder_traversal()
        
	generate_nodes(10, test_bst)
	bst.inorder_traversal()