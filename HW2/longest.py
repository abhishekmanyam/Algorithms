largesubtree = 0

def maximum(value1,value2):
    return max(value1,value2)
def findlargest(tree):
    global largesubtree
    if tree == []:
        return 0
    rightarray = findlargest(tree[2])
    leftarray = findlargest(tree[0]) 
    tree = maximum(leftarray,rightarray) + 1  # finding the depth of the tree
    largesubtree = maximum(largesubtree, leftarray + rightarray )  #finding the max subtree
    return tree

def longest(array):
    global largesubtree
    findlargest(array)
    return largesubtree

print(longest([[[], 1, []], 2, [[], 3, []]]))
