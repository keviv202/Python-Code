class node:
    def __init__(self,n):
        self.val=n
        self.next=None
class queue:
    def __init__(self):
        self.head=  None
        self.tail = None
    def enqueue(self,n):
        if self.head is None:
            self.head = node(n)
            self.tail=self.head

        elif self.head is not None:
            self.tail.next = node(n)
            self.tail = self.tail.next

    def dequeue(self):
        print(self.head.val)
        self.head = self.head.next


    def __str__(self):
        temp = self.head
        ret_str = ""
        while (temp != None):
            ret_str += (str(temp.val))
            temp = temp.next
        return ret_str

q=queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.dequeue()
print(q)
