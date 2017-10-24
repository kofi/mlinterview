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
    
    # returns the number of elements in the linked list 
    # starting the count from the head LLNode till we reach None
    # def size(self):
    #     curr_node = self.head()
    #     count = 0
    #     while curr_node:
    #         count = count+ 1
    #         curr_node = curr_node.next
    #     return count
        

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

def main():
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
    ll.insert_node(50)
    print(question5(ll.head,4))
    #output: None

    # Test 3
    print("Question 5, Test 3:")
    ll = LinkedList()
    print(question5(ll.head,4))
    #output: None

    # Test 4
    print("Question 5, Test 4:")
    for i in range(50):
        ll.insert_node(i)
    print(question5(ll.head,14))
    #output : 13


if __name__ == '__main__':
    main()