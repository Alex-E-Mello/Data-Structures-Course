class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return self.data

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.tallest = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def max_height(self):
        return self.tallest

    def insert(self,item):
        #makes node
        tree_node = TreeNode(item)
        height = 0
        #if tree is empty
        #sets the root
        if self.root == None:
            self.root = tree_node
            self.size = self.size + 1
            print("Adding " + str(self.root.data) + " as the root")

        #if tree isnt empty
        else:
            #starts at the root
            #repeats nonstop
            current = self.root
            while current != None:
                #if node is less than current
                if tree_node.data < current.data:
                    #goes left if it can
                    if current.left_child != None:
                        height = height + 1
                        if height > self.tallest:
                            self.tallest = height
                        current = current.left_child
                    #else it makes the node on left side
                    #returns to leave function
                    else:
                        current.left_child = tree_node
                        current.left_child.parent = current
                        self.size = self.size + 1
                        height = height + 1
                        if height > self.tallest:
                            self.tallest = height
                        print("Adding " + str(tree_node.data) + " to the tree")
                        return
                #if node is greater/equal to current
                if tree_node.data >= current.data:
                    #goes right if it can
                    if current.right_child != None:
                        height = height + 1
                        if height > self.tallest:
                            self.tallest = height
                        current = current.right_child
                    #else it makes the node on the right side
                    #returns to leave function
                    else:
                        current.right_child = tree_node
                        current.right_child.parent = current
                        self.size = self.size + 1
                        height = height + 1
                        if height > self.tallest:
                            self.tallest = height
                        print("Adding " + str(tree_node.data) + " to the tree")
                        return



    def delete(self, item):
        current = self.root
        searching = True

        #if tree is empty
        #returns
        if current == None:
            print("There are no items to delete")

        else:
            while searching == True:
                #if greater than
                if item > current.data:
                    #tries to go right
                    if current.right_child != None:
                        current = current.right_child
                    #if it can't, item isn't in the tree
                    else:
                        print(str(item) + " is not in the tree")
                        return
                #if less than
                if item < current.data:
                    #tries to go left
                    if current.left_child != None:
                        current = current.left_child
                    #if it can't, item isn't in the tree
                    else:
                        print(str(item) + " is not in the tree")
                        return
                #if equal
                if current.data == item:
                    searching = False
                    #if no children
                    if current.left_child == None and current.right_child == None:
                        temp = current
                        current = current.parent
                        temp.parent = None
                        #if greater/equal than parent
                        if item >= current.data:
                            current.right_child = None
                            self.size = self.size - 1
                            print(str(item) + " has been removed from the tree (had no children)")
                            return
                        #if less than parent
                        if item < current.data:
                            current.left_child = None
                            self.size = self.size - 1
                            print(str(item) + " has been removed from the tree (had no children)")
                            return
                    #if left child (not root)
                    if current.left_child != None and current.right_child == None:
                        #makes temp node for item
                        temp = current
                        #changes current to child
                        current = current.left_child
                        #copies parent from temp
                        current.parent = temp.parent
                        #changes parent's child to current
                        if temp.parent.left_child == temp:
                            temp.parent.left_child = current
                        if temp.parent.right_child == temp:
                            temp.parent.right_child = current
                        #removes temp's links
                        temp.parent = None
                        temp.left_child = None
                        self.size = self.size - 1
                        print(str(item) + " has been removed from the tree (had left child)")
                        return
                    #if right child (not root)
                    if current.right_child != None and current.left_child == None:
                        #makes temp node for item
                        temp = current
                        #changes current to child
                        current = current.right_child
                        #copies parent from temp
                        current.parent = temp.parent
                        #changes parent's child to current
                        if temp.parent.left_child == temp:
                            temp.parent.left_child = current
                        if temp.parent.right_child == temp:
                            temp.parent.right_child = current
                        #removes temp's links
                        temp.parent = None
                        temp.right_child = None
                        self.size = self.size - 1
                        print(str(item) + " has been removed from the tree (had right child)")
                        return
                    #if two children
                    if current.right_child != None and current.left_child != None:
                        results = self.traverse_inorder()
                        for each in results:
                            if each > item:
                                self.delete(each)
                                current.data = each                                
                                print(str(item) + " has been replaced by " + str(each) + " (had both children)")
                                return
                                    


    def __contains__(self,item):
        current = self.root
        
        #if tree is empty
        #returns False
        if current == None:
            return False
        
        #else
        else:
            #calls traverse inorder
            tree_items = self.traverse_inorder()
            #returns a list that is in order smallest -> largest
            #for each in list
            for test in tree_items:
                #if the current test is bigger than the item
                #returns False
                if item < test:
                    return False
                #else if the item is found
                #returns True
                else:
                    if item == test:
                        return True
                    
        #safety net
        #returns False if item wasn't found
        return False



    def traverse_inorder(self, node=None,results=None):
        #if node isn't given
        #sets node as root
        if node == None:
            current = self.root
        else:
            current = node

        #if results list isn't passed
        #starts a list
        if results == None:
            results = []
        else:
            results = results

        #if there is a left child
        #recursive call using tree starting with left child
        #also passes the results list
        if current.left_child != None:
            self.traverse_inorder(current.left_child,results)

        #adds current to list
        results.append(current.data)

        #if there is a right child
        #recursive call using tree starting with right child
        #also passes the results list        
        if current.right_child != None:
            self.traverse_inorder(current.right_child,results)

        #returns list of items in list
        return results

    def traverse_preorder(self,node=None,results=None):
        if node == None:
            current = self.root
        else:
            current = node

        if results == None:
            results = []
        else:
            results = results

        results.append(current.data)

        if current.left_child != None:
            self.traverse_preorder(current.left_child,results)
        
        if current.right_child != None:
            self.traverse_preorder(current.right_child,results)

        return results

    def traverse_postorder(self,node=None,results=None):
        if node == None:
            current = self.root
        else:
            current = node

        if results == None:
            results = []
        else:
            results = results

        if current.left_child != None:
            self.traverse_postorder(current.left_child,results)        

        if current.right_child != None:
            self.traverse_postorder(current.right_child,results)

        results.append(current.data)
        return results



def main():
    tree = BinaryTree()

    tree.insert(50)
    tree.insert(75)
    tree.insert(25)
    tree.insert(40)   
    tree.insert(60)
    tree.insert(90)
    tree.insert(85)
    tree.insert(95)
    tree.insert(10)
    tree.insert(20)

    print()
    print("The length of the tree is " + str(len(tree)))
    print("The max height of the tree is " + str(tree.max_height()))

    print()
    test = 90
    if test in tree:
        print(str(test) + " is in the tree")
    else:
        print(str(test) + " is not in the tree")

    print()
    print("Removing 90 from the tree")
    tree.delete(90)

    print()
    test = 90
    if test in tree:
        print(str(test) + " is in the tree")
    else:
        print(str(test) + " is not in the tree")

    print()
    print("Removing 10 from the tree")
    tree.delete(10)

    print()
    print("Removing 85 from the tree")
    tree.delete(85)

    print()
    print("The length of the tree is " + str(len(tree)))
    print("The max height of the tree is " + str(tree.max_height()))

    print()
    print("Inorder Traversal")
    print(str(tree.traverse_inorder()))

    print()
    print("Preorder Traversal")
    print(str(tree.traverse_preorder()))

    print()
    print("Postorder Traversal")
    print(str(tree.traverse_postorder()))

main()




















