class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

head = a1
cur = a1


print('Before')
while cur != None:
    print(cur.val)
    cur = cur.next


# a5.next = a1
# a4.next = None
# head = a5

# a5.next = a4
# a4.next = a1
# a3.next = None

# a4.next = a3
# a3.next = a1
# a2.next = None

# a3.next = a2
# a2.next = a1
# a1.next = None

#find end of list 

cur = head
while cur != None:
    if cur.next == None:
        n5 = head
        n5.next = head





cur = head
print('AFter')
while cur != None:
    print(cur.val)
    cur = cur.next

