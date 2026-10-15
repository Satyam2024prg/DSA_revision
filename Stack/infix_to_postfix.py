from stack import Stack


def infix_to_postfix(infix_expression):

  stack  = Stack()
  postfix_list = []
  precedence = {
    '(' : 1,
    '+' : 2,
    '-' : 2,
    '*' : 3,
    '/' : 3,
    '^' : 4
  }

  # token_list = infix_expression.split()  # work when spaces are between them

  token_list = list(infix_expression)
  # print(token_list)
  # print(infix_expression)
  
  for token in token_list:
    if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
      postfix_list.append(token)
    elif token == '(':
      stack.push(token)
    elif token == ')':
      top_token = stack.pop()
      while top_token != '(':
        postfix_list.append(top_token)
        top_token = stack.pop()
    else:
      while not stack.is_empty() and precedence[stack.peek()] >= precedence[token]:
        postfix_list.append(stack.pop())
      stack.push(token)

  while not stack.is_empty():
    postfix_list.append(stack.pop())
  return " ".join(postfix_list)

print(infix_to_postfix('A*B+C/D'))
print(infix_to_postfix('A+B*C'))