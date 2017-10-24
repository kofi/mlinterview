parent = dict()
rank = dict()

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

# Main program
def main():
    
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

if __name__ == '__main__':
    main()
