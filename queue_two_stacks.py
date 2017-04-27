"""A tale of two stacks:
implementing a queue using two stacks
"""
class MyQueue(object):
    def __init__(self):
        self.first = []  # new items
        self.second = []  # old items
    
    def peek(self):
        """See the oldest value in the queue"""
        if not self.second:
            self.empty_first()
        return self.second[-1]
            
        
    def pop(self):
        """Pop the oldest value from the queue"""
        if not self.second:
            self.empty_first()
        self.second.pop()
        
    def put(self, value):
        """Add a value to the queue"""
        self.first.append(value)
    
    def empty_first(self):
        """Pop from first stack, append to second stack"""
        while self.first:
                self.second.append(self.first.pop())

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()