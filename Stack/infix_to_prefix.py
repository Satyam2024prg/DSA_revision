from stack import Stack

def infix_to_prefix(infix_expression):
  stack = Stack()
  reversed_prefix_list = []
  precedence = {
      ')' : 1,
      '+' : 2,
      '-' : 2,
      '*' : 3,
      '/' : 3
    }
  
  reversed_expression = infix_expression[::-1]
  reversed_expression_list = list(reversed_expression)
  # print(reversed_expression_list)

  for token in reversed_expression_list:
    if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
      reversed_prefix_list.append(token)
    elif token == ')':
      stack.push(token)
    elif token == '(':
      top_token = stack.pop()
      while top_token != ')':
        reversed_prefix_list.append(top_token)
        top_token = stack.pop()
    else:
      while not stack.is_empty() and precedence[stack.peek()] >= precedence[token]:
        reversed_prefix_list.append(stack.pop())
      stack.push(token)

  while not stack.is_empty():
    reversed_prefix_list.append(stack.pop())
  prefix_list = reversed_prefix_list[::-1]
  return " ".join(prefix_list)

print(infix_to_prefix('(A*B)+(C/D)'))