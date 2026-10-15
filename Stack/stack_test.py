from stack import Stack

s = Stack()

s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.peek())
print(s.size())
print(s.is_empty())
s.pop()
s.pop()
print(s.peek())
print(s.size())