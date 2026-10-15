from stack import Stack

def par_checker(symbol_string):
  s = Stack()
  index = 0
  balanced = True

  while index < len(symbol_string) and balanced:
    symbol = symbol_string[index]
    if symbol == '(' or symbol == '[' or symbol == '{':
      s.push(symbol)
    else : 
      if s.is_empty():
        balanced = False
      elif symbol == ')' and s.peek() == '(' or symbol == '}' and s.peek() == '{' or symbol == ']' and s.peek() == '[':
        s.pop()
      else:
        balanced = False
    

    index += 1

  if balanced and s.is_empty():
    return True
  else:
    return False

print(par_checker('({[]})'))
print(par_checker('(){}[]'))
print(par_checker('({)}[(])'))
print(par_checker('({[)]}'))
print(par_checker('[({})]'))
print(par_checker('()}]'))
print(par_checker(')'))
print(par_checker("({)}"))