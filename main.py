# class for the nodes of the tree
class TreeNode:

    # constructor for each node, including optional parameters
    def __init__(self, parent=None, left=None, right=None, data=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    # many setters and getters for each attribute of the tree's nodes
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setRight(self, right):
        self.right = right

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


# class for the tree structure itself
class Tree:

    # constructor for Tree itself, including optional parameter
    def __init__(self, root=None):
        self.root = root

    # setters and getters
    def setRoot(self, root):
        self.root = root

    def getRoot(self):
        return self.root

    # adapted from Cormen, et al "Introduction to Algorithms", pg294
    def insert(self, node):

        # a trailing node (to stay behind currNode)
        trailNode = None

        # begins process at root
        currNode = self.root

        # while the current node is not None
        while currNode is not None:

            # sets the trailing node to where we currently are
            trailNode = currNode

            # and checks to see which "branch" to traverse
            # (right or left) based on values
            if node.getData() < currNode.getData():
                currNode = currNode.getLeft()
            else:
                currNode = currNode.getRight()

        # sets parent accordingly but also checks if trailNode is None
        # meaning we are at root and we set the node to this tree's
        # root
        node.setParent(trailNode)
        if trailNode is None:
            self.setRoot(node)

        # else checks to see where the proper insertion point is, based
        # on value of node and trailNode
        elif node.getData() < trailNode.getData():
            trailNode.setLeft(node)
        else:
            trailNode.setRight(node)

    # adapted from Cormen, et al "Introduction to Algorithms", pg288.
    # uses inorder-tree-walk; instead of printing, checks for improper
    # order of BST and immediately returns false if detected
    def recursiveSatisfaction(self, node, counter):
        if node is not None:
            counter[0] += 1
            # if node.getLeft() is not None and node.getRight() is not None:
                #counter[0] += 1
            if node.getLeft() is not None and node.getLeft().getData() > node.getData():
                return False
            self.recursiveSatisfaction(node.getLeft(), counter)
            #counter[0] += 1
            if node.getRight() is not None and node.getRight().getData() < node.getData():
                return False
            self.recursiveSatisfaction(node.getRight(), counter)
            counter[0] += 1
        return True

    # adapted from Cormen, et al "Introduction to Algorithms", pg288;
    # just prints in order (according to proper BST)
    def inOrderPrint(self, node):
        if node is not None:
            self.inOrderPrint(node.getLeft())
            print(node.getData())
            self.inOrderPrint(node.getRight())


def main():

    # use array of ints, then array of TreeNode objects, to make forming
    # the trees a bit easier (with for loops)
    tree1Data = [16, 10, 8, 2, 14, 15, 25, 20, 22, 30, 27]
    tree2Data = [7, 10, 1, 12, 13, 14, 5, 6, 3, 2, 4]
    tree1Nodes = []
    tree2Nodes = []

    for i in range(0, 11):
        tree1Nodes.append(TreeNode(None, None, None, tree1Data[i]))
        tree2Nodes.append(TreeNode(None, None, None, tree2Data[i]))

    # set root of both trees
    tree1 = Tree(tree1Nodes[0])
    tree2 = Tree(tree2Nodes[0])

    # insert works nicely, using the TreeNode objects from tree1Nodes
    for j in range(1, 11):
        tree1.insert(tree1Nodes[j])

    # this is gross but my insert method works properly so this is
    # the only way to create tree2 (the one that is not a BST)
    tree2.getRoot().setLeft(tree2Nodes[1])
    tree2.getRoot().getLeft().setLeft(tree2Nodes[2])
    tree2.getRoot().getLeft().getLeft().setRight(tree2Nodes[3])
    tree2.getRoot().getLeft().setRight(tree2Nodes[4])
    tree2.getRoot().getLeft().getRight().setLeft(tree2Nodes[5])
    tree2.getRoot().setRight(tree2Nodes[6])
    tree2.getRoot().getRight().setLeft(tree2Nodes[7])
    tree2.getRoot().getRight().getLeft().setRight(tree2Nodes[8])
    tree2.getRoot().getRight().setRight(tree2Nodes[9])
    tree2.getRoot().getRight().getRight().setRight(tree2Nodes[10])

    print("The binary search tree printed in order:")
    tree1.inOrderPrint(tree1.getRoot())
    counter = [0]
    if tree1.recursiveSatisfaction(tree1.getRoot(), counter):
        print("\nNice! This tree is a binary search tree!")
    else:
        print("Something has gone horribly wrong.")
    print("This algorithm runs", counter[0], "times; or 2n, where n is"
          " 11 nodes. So, O(n) running time.\n")

    counter[0] = 0
    print("The tree that is not a BST, printed in what this method"
          " believes is\ncorrectly-sorted order:")
    tree2.inOrderPrint(tree2.getRoot())
    if tree2.recursiveSatisfaction(tree2.getRoot(), counter):
        print("How did that happen?\n")
    else:
        print("\nNo, that's not a binary search tree.")
    print("The algorithm also runs in O(n) time here, as well. However,"
          " it actually\nonly runs", counter[0], "time for the first node;"
          " from there, it checks the root's left;\n10 is greater than"
          " 7, and so returns false, only having ran once.")


if __name__ == "__main__":
    main()