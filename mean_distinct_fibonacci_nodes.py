# Mean of distinct odd fibonacci nodes in a Linked List
# Given a singly linked list containing N nodes, the task is to find the mean of all the distinct nodes from the list whose data value is an odd Fibonacci number.


# Python3 program to implement
# the above approach

# Structure of a
# singly Linked List
class Node:

    def __init__(self):
        # Stores data value
        # of a Node
        self.data = 0

        # Stores pointer
        # to next Node
        self.next = None


# Function to add a node at the
# beginning of the singly Linked List
def push(head_ref, new_data):
    # Create a new Node
    new_node = Node()

    # Insert the data into
    # the Node
    new_node.data = new_data;

    # Insert pointer to
    # the next Node
    new_node.next = head_ref

    # Update head_ref
    head_ref = new_node;

    return head_ref


# Function to find the largest
# element from the linked list
def largestElement(head_ref):
    # Stores the largest element
    # in the linked list
    Max = -10000000

    head = head_ref;

    # Iterate over the linked list
    while (head != None):

        # If max is less than
        # head.data
        if (Max < head.data):
            # Update  max
            Max = head.data;

        # Update head
        head = head.next;

    return Max;


# Function to store all Fibonacci numbers
# up to the largest element of the list
def createHashMap(Max):
    # Store all Fibonacci numbers
    # up to Max
    hashmap = set()

    # Stores first element of
    # Fibonacci number
    prev = 0;

    # Stores second element of
    # Fibonacci number
    curr = 1;

    # Insert prev into hashmap
    hashmap.add(prev);

    # Insert curr into hashmap
    hashmap.add(curr);

    # Insert all elements of
    # Fibonacci numbers up to Max
    while (curr <= Max):
        # Stores current fibonacci number
        temp = curr + prev;

        # Insert temp into hashmap
        hashmap.add(temp);

        # Update prev
        prev = curr;

        # Update curr
        curr = temp;

    return hashmap;


# Function to find the mean
# of odd Fibonacci nodes
def meanofnodes(head):
    # Stores the largest element
    # in the linked list
    Max = largestElement(head);

    # Stores all fibonacci numbers
    # up to Max
    hashmap = createHashMap(Max);

    # Stores current node
    # of linked list
    curr = head;

    # Stores count of
    # odd Fibonacci nodes
    cnt = 0;

    # Stores sum of all
    # odd fibonacci nodes
    sum = 0.0;

    # Traverse the linked list
    while (curr != None):

        # if the data value of
        # current node is an odd number
        if ((curr.data) % 2 == 1):

            # if data value of the node
            # is present in hashmap
            if (curr.data in hashmap):
                # Update cnt
                cnt += 1

                # Update sum
                sum += curr.data;

                # Remove current fibonacci number
                # from hashmap so that duplicate
                # elements can't be counted
                hashmap.remove(curr.data);

        # Update curr
        curr = curr.next;

    # Return the required mean
    return (sum / cnt);


# Driver Code
if __name__ == '__main__':
    # Stores head node of
    # the linked list
    head = None;

    # Insert all data values
    # in the linked list
    head = push(head, 5);
    head = push(head, 21);
    head = push(head, 8);
    head = push(head, 12);
    head = push(head, 3);
    head = push(head, 13);
    head = push(head, 144);
    head = push(head, 6);

    print(meanofnodes(head))
