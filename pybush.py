from binarytree import *


# A new definition of class to get more trees function
class Node(Node):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.h = self.height
        self.count = 1


# Tree Root
root = [None]


# # # # AVL # # # # #

# returns updated height of the tree, doesn't update height
def check_height(pointer):
    if pointer:
        if pointer.left and pointer.right:
            return 1 + max(pointer.left.h, pointer.right.h)

        elif pointer.left:
            return 1 + pointer.left.h
        elif pointer.right:
            return 1 + pointer.right.h
        else:
            return 0
    else:
        return -1


# Check whether the node follows avl property
def avl(pointer):
    if abs(check_height(pointer.left) - check_height(pointer.right)) < 2:
        #print("AVL OKAY")
        return True
    else:
        #print("AVL VIOLATED")
        return False


# Rotate function : For insertion, Delete
def rotate(pointer):
    c = 0
    z = pointer
    if check_height(z.left) + 1 == z.h:
        y = z.left
    else:
        y = z.right
        c += 2

    if check_height(y.left) + 1 == y.h:
        x = y.left
    else:
        x = y.right
        c += 1

    if c == 0:
        if z.parent:
            if z.parent.left == z:
                z.parent.left = y
            else:
                z.parent.right = y

        else:
            y.parent = None
            root[0] = y

        t3 = y.right
        y.right = z
        z.left = t3
        y.parent = z.parent
        z.parent = y
        if t3:
            t3.parent = z
        z.h = check_height(z)
        x.h = check_height(x)
        y.h = check_height(y)
        assign_count(y)

    elif c == 3:
        if z.parent:
            if z.parent.left == z:
                z.parent.left = y
            else:
                z.parent.right = y

        else:
            y.parent = None
            root[0] = y

        t2 = y.left
        y.left = z
        z.right = t2
        y.parent = z.parent
        z.parent = y
        if t2:
            t2.parent = z
        z.h = check_height(z)
        x.h = check_height(x)
        y.h = check_height(y)
        assign_count(y)

    elif c == 1:
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x

        else:
            x.parent = None
            root[0] = x

        t2 = x.left
        t3 = x.right
        y.right = t2
        z.left = t3
        x.parent = z.parent
        z.parent = x
        y.parent = x
        if t2:
            t2.parent = y
        if t3:
            t3.parent = z

        x.left = y
        x.right = z

        z.h = check_height(z)
        x.h = check_height(y)
        y.h = check_height(x)
        assign_count(x)

    elif c == 2:
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x

        else:
            x.parent = None
            root[0] = x

        t2 = x.left
        t3 = x.right
        y.left = t3
        z.right = t2
        x.parent = z.parent
        z.parent = x
        y.parent = x
        if t2:
            t2.parent = z
        if t3:
            t3.parent = y

        x.left = z
        x.right = y

        z.h = check_height(z)
        x.h = check_height(y)
        y.h = check_height(x)
        assign_count(x)


# delete node in avl
def delete_avl(pointer, x):
    if search(pointer, x):
        while pointer:
            pointer.count -= 1
            if pointer.value == x:
                return delete_node_avl(pointer)
            elif pointer.value > x:
                pointer = pointer.left
            else:
                pointer = pointer.right
    else:
        print("x not in the tree")


# is called by delete_avl, uses rotation to maintain avl properties
def delete_node_avl(pointer):
    if pointer.left and pointer.right:
        replace_ele = pointer.left
        while replace_ele.right is not None:
            replace_ele.count -= 1
            replace_ele = replace_ele.right

        pointer.value = replace_ele.value
        pointer = replace_ele

    p = pointer.parent

    if pointer.left:
        child = pointer.left
    else:
        child = pointer.right

    if root == pointer:
        child.parent = None
        root[0] = child

    if child:
        child.parent = p

    if p:
        if p.left == pointer:
            p.left = child
        else:
            p.right = child

    temp = p
    if p:
        flag = True
    else:
        flag = False

    while flag:
        if not avl(temp):
            rotate(temp)
            temp = temp.parent.parent

            if not temp:
                flag = False

        else:
            h = check_height(temp)
            if h < temp.h:
                temp.h = h

                if temp.parent:
                    temp = temp.parent
                else:
                    flag = False

            else:
                flag = False

    del pointer


# Insert a node(x) in avl, uses rotation to maintain avl properties
def add_avl(pointer, x):
    if pointer.value < x:
        if pointer.right is not None:
            pointer.count += 1
            return add_avl(pointer.right, x)
        else:
            pointer.count += 1
            pointer.right = Node(x)
            pointer.right.parent = pointer

    elif pointer.value > x:
        if pointer.left is not None:
            pointer.count += 1
            return add_avl(pointer.left, x)
        else:
            pointer.count += 1
            pointer.left = Node(x)
            pointer.left.parent = pointer

    #print("NODE ADDED")
    temp = pointer

    flag = True
    while flag:
        h = check_height(temp)
        #print(h, temp.h)

        if h > temp.h:
            temp.h = h

            if not avl(temp):
                rotate(temp)
                #print("ROTATED")
                flag = False

            elif temp.parent:
                #print("MOVING UP")
                temp = temp.parent

            else:
                #print("NO VIOLATION OF AVL TILL ROOT")
                flag = False

        else:
            #print("NO CHANGE IN HEIGHT")
            flag = False

    #print("END OF WHILE")


# given a tree, it will change node.h to it's actual height
def assign_height(pointer):
    if pointer is None:
        return -1
    else:
        left_height = assign_height(pointer.left)
        right_height = assign_height(pointer.right)

    pointer.h = max(right_height, left_height) + 1
    return max(right_height, left_height) + 1


# given a tree, it will update node.count
def assign_count(pointer):
    if pointer is None:
        return 0
    else:
        left_count = assign_count(pointer.left)
        right_count = assign_count(pointer.right)

    pointer.count = right_count + left_count + 1
    return right_count + left_count + 1


# find rank
def rank(pointer, x):
    r = 1
    while pointer:
        if pointer.value == x:
            if pointer.right:
                r += pointer.right.count
            return r
        elif pointer.value > x:
            r += 1
            if pointer.right:
                r += pointer.right.count
            pointer = pointer.left
        else:
            pointer = pointer.right
    return r


# given a rank, find the element
def find_rank(pointer, frank):
    if pointer and 0 < frank < pointer.count + 1:
        while pointer:
            if pointer.right:
                r = pointer.right.count + 1
            else:
                r = 1
            if r == frank:
                return pointer
            elif frank > r:
                pointer = pointer.left
                frank = frank - r
            else:
                pointer = pointer.right
    return None


# gives no. of elements in the range of l and r
def rangecount(pointer, l, r):
    count = rank(pointer, l) - rank(pointer, r)

    if search(pointer, l):
        count += 1

    return count


# check whether a tree or subtree is a avl tree
def is_avl(pointer):
    if pointer is None:
        return True

    if (avl(pointer)) and is_avl(pointer.left) is True and is_avl(pointer.right) is True:
        return True

    return False


# given a tree, find the maximum avl subtree
def largest_avl_subtree(pointer):
    if pointer:
        if is_avl(pointer):
            return pointer

        else:
            left = largest_avl_subtree(pointer.left)
            right = largest_avl_subtree(pointer.right)

            if left and right:
                if left.h > right.h:
                    return left
                else:
                    return right

            elif left and not right:
                return left

            elif not left and right:
                return right

            else:
                return None

    else:
        return None


# # # # # BST # # # # #


# Create a balance binary search tree : returns root node
# Tree is without node.h and node.count
def bbst(arr, l, r):
    if l <= r:
        m = (l + r) // 2
        node = Node(arr[m])
        node.left = bbst(arr, l, m - 1)
        node.right = bbst(arr, m + 1, r)

        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node

        return node

    else:
        return None


# create a bbst with all the attributes, height, parent, count
def create_bbst(arr, l, r):
    root_node = bbst(arr, l, r)
    assign_parent(root_node)
    assign_height(root_node)
    assign_count(root_node)
    root[0] = root_node
    return root_node


# Predecessor of x
def predecessor(root, x):
    ele = search(root, x)
    if ele is None:
        return None

    elif ele.left:
        ele = ele.left
        while ele.right is not None:
            ele = ele.right
        return ele

    else:
        while ele.parent:
            if ele.parent.right == ele:
                break
            else:
                ele = ele.parent

        return ele.parent


# Successor of x
def successor(root, x):
    ele = search(root, x)

    if ele is None:
        return None

    elif ele.right:
        ele = ele.right
        while ele.left is not None:
            ele = ele.left
        return ele

    else:
        while ele.parent:
            if ele.parent.left == ele:
                break
            else:
                ele = ele.parent

        return ele.parent


# Least common ancestor
def lca(pointer, l, r):
    left = search(pointer, l)
    right = search(pointer, r)
    if pointer is None or left.value > right.value or left is None or right is None:
        return None

    if pointer.value > right.value:
        return lca(pointer.left, l, r)

    if pointer.value < left.value:
        return lca(pointer.right, l, r)

    return pointer


# in arr, appends the range
def rangelist(pointer, l, r, arr):
    if pointer:

        if pointer.value > r:
            rangelist(pointer.left, l, r, arr)
        elif pointer.value < l:
            rangelist(pointer.right, l, r, arr)

        else:
            rangelist(pointer.right, l, r, arr)
            arr.append(pointer)
            rangelist(pointer.left, l, r, arr)


# counts no. of elements between l and r
def rangecount(pointer, l, r):
    if pointer is None or l > r:
        return 0

    if pointer.value > r:
        return rangecount(pointer.left, l, r)

    if pointer.value < l:
        return rangecount(pointer.right, l, r)

    return 1 + rangecount(pointer.left, l, r) + rangecount(pointer.right, l, r)


# search in avl,bst,bbst
def search(pointer, x):
    if pointer is not None:
        if pointer.value == x:
            return pointer
        elif pointer.value < x:
            return search(pointer.right, x)
        elif pointer.value > x:
            return search(pointer.left, x)
    else:
        return None


# add node(x), maintaing the bst properties
def add(pointer, x):
    if pointer.value < x:
        if pointer.right is not None:
            return add(pointer.right, x)
        else:
            pointer.right = Node(x)
            pointer.right.parent = pointer
            return pointer.right
    elif pointer.value > x:
        if pointer.left is not None:
            return add(pointer.left, x)
        else:
            pointer.left = Node(x)
            pointer.left.parent = pointer
            return pointer.left


# Delete the node(x), maintaing the bst properties
def delete(root, x):
    pointer = root
    while pointer:
        if pointer.value == x:
            return delete_node(root, pointer)
        elif pointer.value > x:
            pointer = pointer.left
        else:
            pointer = pointer.right


# called by delete function
def delete_node(root, pointer):
    if pointer.left and pointer.right:
        replace_ele = pointer.left
        while replace_ele.right is not None:
            replace_ele = replace_ele.right

        pointer.value = replace_ele.value
        pointer = replace_ele

    p = pointer.parent

    if pointer.left:
        child = pointer.left
    else:
        child = pointer.right

    if root == pointer:
        child.parent = None
        root[0] = child

    if child:
        child.parent = p

    if p:
        if p.left == pointer:
            p.left = child

        else:
            p.right = child




# given a tree, assign parents to each nodes
def assign_parent(root):
    if root.left is not None:
        root.left.parent = root
        # print(root.left.value)

    if root.right is not None:
        root.right.parent = root
        # print(root.right.value)

    if root.left is not None:
        assign_parent(root.left)

    if root.right is not None:
        assign_parent(root.right)

# # # # # # # # # # END OF FUNCTIONS # # # # # # # # # # #
