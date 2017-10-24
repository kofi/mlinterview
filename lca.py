# return the least common ancestor for two nodes
def get_lca_for_nodes(T,h,n1,n2):
    # assumption is both nodes are in the tree
    # ... and the tree is a valid BST
    # checks 
    if h is None:
        return None
 
    # using BST properties if both elements identify branch of tree to search
    # search right branch if both are greater than root value
    curr_node = h 
    while (curr_node > n1 and curr_node > n2):
        curr_node = get_left_node(T, curr_node)
        if curr_node is None:
            break

    # search left branch if both are greater than root value
    while (curr_node < n1 and curr_node < n2 ):
        curr_node = get_right_node(T, curr_node)
        if curr_node is None:
            break

    return curr_node
    
def get_right_node(T,node):
    node_value = node+1
    new_node = None 
    if node+1 > len(T[node])-1:
        return new_node
    for val in T[node][node+1:]:
        if val:
            new_node = node_value
            break
        node_value = node_value + 1
    return new_node

def get_left_node(T,node):
    node_value = 0 
    new_node = None 
    for val in T[node][0:node-1]:
        if val:
            new_node = node_value
            #print(node_value)
            break
        node_value = node_value + 1
    return new_node

def question4(T,r,n1,n2):
    #global T
    if len(T) == 0 or T is None:
        return None
    if r is None or n1 is None or n2 is None:
        return None

    return get_lca_for_nodes(T,r, n1, n2)

def main():

    print("Question4, Test1:")
    print(question4([  [0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0]],
                        3,
                        1,
                        4))
    # output : 3

    print("Question4, Test2:")
    print(question4([[0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0]],
                    None,
                    2,
                    4))
    # output : None 

    print("Question4, Test3:")
    print(question4([],
                    3,
                    1,
                    4))
    # output : None

    print("Question4, Test4:")
    print(question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ],
                    6,
                    7,
                    8))
    # output : 8

    print("Question4, Test5:")
    print(question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ],
                    6,
                    7,
                    9))
    # output : 8

    print("Question4, Test6:")
    print(question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ],
                    6,
                    3,
                    5))
    # output : 4

if __name__ == '__main__':
    main()


       