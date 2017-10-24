import sys

parent = dict()
rank = dict()


class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str((self.data, 'next:', self.next))
    __repr__ = __str__

    # # add a new node as the next node
    # def insert_next(node):
    #     self.next = next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = None
    
    # add a node to the LinkedList.
    # this becomes the new head
    def insert_node(self, data):
        node = LLNode(data)
        node.next = self.head
        self.head = node
    

def question5(head,n):
    
    if head is None:
        return None
    # counter for tracking the size of the sliding window
    count = 0
    # set both start and end nodes to the head
    window_start = head
    window_end = head
    if window_end is None:
        return None

    while count < n:
        # create a sliding window of length n and find the node at the window end. Remember the window will be size n
        if window_end is None:
            return None
        
        window_end = window_end.next
        count = count + 1

    # start moving the window start till window_end becomes None
    # then window start will be size n from the end of the LinkedList    
    while window_end is not None:
        window_start = window_start.next
        window_end = window_end.next
    
    return window_start.data

######################################################################

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

######################################################################

# create a tree with a single vertex
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

# find the set which contains a specific vertex
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

# implements function to perform a union of two sets using the rank
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

# convert the graph from the dictionary adjacency matrix to
# an array of tuples so we can sort readily
def convert_graph(in_graph):
    graph = []
    for i in in_graph:
        for j in in_graph[i]:
            weight, vertice1, vertice2 = j[1], i, j[0] #in_graph[i][j][0]
            graph.append((weight, vertice1, vertice2))
    
    return graph

# implements Kruskal's algorithm for generate a minimum spanning tree (MST)
def question3(s1):
    if s1 is None or len(s1) == 0:
        return {}

    # create a set with single elements
    # the algorithm will then try to join different sets in creating the MST
    for vertice in s1.keys(): #O(NE)
        make_set(vertice)

    mst = {} 
    # convert graph so it is easier to sort the graph and iterate over edges
    edges = convert_graph(s1) # worst case O(NE) where NE is the # of edges
    # sort the graph
    edges.sort() # NE*log(NE)

    for edge in edges: # O(NE*log(NV)) where NV is the number of vertices
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2) 
            if vertice1 not in mst:
                mst[vertice1] = []
            mst[edge[1]].append((edge[2], edge[0]))
    return mst

######################################################################

def search_from_indices(s, i, j):
    left = i
    right = j
    while (left >=0 and right <= len(s)-1 and s[left].lower()==s[right].lower()):
        left = left -1 
        right = right + 1

    return s[left+1:right]

def question2(s):
    if len(s) == 0 or s is None:
        return ''
    palindrome = s[0:1]
    #print(palindrome)
    for i in range(len(s)-1):
        #print(i)
        curr_pal = search_from_indices(s,i,i)
        #print(curr_pal)
        if len(curr_pal) > len(palindrome):
            palindrome = curr_pal 
            #print(palindrome)
        curr_pal = search_from_indices(s,i,i+1)
        #print(curr_pal)
        if len(curr_pal) > len(palindrome):
            palindrome = curr_pal 
            #print(palindrome)

    return palindrome

######################################################################

def is_anagram(s1, t_dict):
    '''
        a string is an anagram of another if they contain the same letters
        quick way to check is to sort the two strings and compare them
        this function uses pythons in-built quick sort
        and returns True if the two strings are anagrams
    '''
    if len(s1) != len(t_dict):
        return False
    for i in s1:
        if i not in t_dict:
            return False
        else:
            t_dict[i] = t_dict[i] - 1
    
    if sum(t_dict.values()) == 0:
        return True
    return False

def question1(s,t):
    if s is None or t is None:
            return False
    if len(t) > len(s):
        return False
    if len(s) == 0 or len(t)==0:
        return False

    # loop over the input string and take slices of length = length(substring)
    # check if the two substrings match
    t_dict = {}
    for j in t:
        if j not in t_dict:
            t_dict[j] = 1
        else :
            t_dict[j] = t_dict[j] + 1

    for i in range(len(s)-len(t)+ 1):
        segment = s[i:i+len(t)]
        if is_anagram(segment,t_dict):
            return True

######################################################################

# Main program
def main():
    print("Question 1, Test 1")
    print(question1("udacity", "ad"))
    # output : True

    print("Question 1, Test 2")
    print question1("", "de")
    #output : False

    print("Question 1, Test 3")
    print question1("udacity", "")
    #output : False

    print

    ######################################################################

    s = 'abrACaDaBRa'
    print('Question 2, Test 1')
    print(question2(s))
    # output: ACa 
    
    s = ''
    print('Question 2, Test 2')
    print(question2(s))
    # output : ''
    
    s='FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    print('Question 2, Test 3')
    print(question2(s))
    # #output : ranynar
    print

    ######################################################################

    # Test 1
    s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    print("Question 3, Test 1")
    print(question3(s1))
    # {'A': [('B', 2)], 'B': [('C', 2)]}
    
    # Test 2
    # s2 = {'A': [('B', 1)],
    #     'B': [('A', 4), ('C', 2)],
    #     'C': [('A', 2), ('B', 5)],
    #     'D': [('C', 3), ('B', 1), ('A',2)]}
    print("Question 3, Test 2")
    s1 = {'A':[]}
    print(question3(s1))
    # output : {}

    # Test 3
    s1 = {}
    print("Question 3, Test 3")
    print(question3(s1))
    # output : {}
    print

    ######################################################################

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
    
    print

    ######################################################################

    print("Question 5, Test 1:")
    # Test 1
    ll = LinkedList()
    ll.insert_node(50)
    ll.insert_node(40)
    ll.insert_node(30)
    ll.insert_node(20)
    ll.insert_node(10)
    #print(ll .head)
    print(question5(ll.head,4))
    #output: 20


    # Test 2
    print("Question 5, Test 2:")
    ll = LinkedList()
    print(question5(ll.head,4))
    #output: None

    # Test 3
    print("Question 5, Test 3:")
    for i in range(50):
        ll.insert_node(i)
    print(question5(ll.head,14))
    #output : 13


if __name__ == '__main__':
    main()
