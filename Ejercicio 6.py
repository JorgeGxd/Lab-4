class newNode:
     
    def __init__(self, item):
         
        self.key = item
        self.left = None
        self.right = None
 
def insert(node, key):
     

    if (node == None):
        return newNode(key)
 

    if (key < node.key):
        node.left = insert(node.left, key)
 

    elif(key > node.key):
        node.right = insert(node.right, key)
 
 
    return node
 

def KSmallestPerfectBST(root, k, treeSize):
     
    global kth_smallest
     
    if (root == None):
        return False
 
  
    median_loc = (treeSize // 2) + 1
 
  
    if (k == median_loc):
        kth_smallest = root.key
        return True
 

    newTreeSize = treeSize // 2
 

    if (k < median_loc):
        return KSmallestPerfectBST(root.left,
                                   k, newTreeSize)
 

    newK = k - median_loc
    return KSmallestPerfectBST(root.right, newK,
                               newTreeSize)
 

if __name__ == '__main__':
     
    ''' Let us create following BST
              50
           /       \
          30        70
         /  \      /  \
       20   40    60    80
       /\   /\    /\    / \
     14 25 35 45 55 65 75  85
    '''
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 14)
    insert(root, 25)
    insert(root, 35)
    insert(root, 45)
    insert(root, 55)
    insert(root, 65)
    insert(root, 75)
    insert(root, 85)
 
    n = 15
    k = 5
   
    if (KSmallestPerfectBST(root, k, n)):
        print(kth_smallest, end = " ")