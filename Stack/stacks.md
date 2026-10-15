A. Infix to Postfix Conversion Algorithm

Read the expression from left to right.
1. If an operand (A-Z, 0-9) is encountered, add it directly to the output.
2. If an operator is encountered:
   1. Pop operators from the stack to the output if they have higher or equal precedence.
   2. Push the current operator onto the stack.
3. If an opening parenthesis ( is found, push it onto the stack.
4. If a closing parenthesis ) is found, pop operators from the stack to the output until an opening parenthesis is encountered.
5. After scanning the entire expression, pop any remaining operators from the stack to the output.




B. Convert Infix to Prefix Expression

At first infix expression is reversed. Note that for reversing the opening and closing parenthesis will also be reversed.

for an example: The expression: A + B * (C - D)

after reversing the expression will be: ) D – C ( * B + A

so we need to convert opening parenthesis to closing parenthesis and vice versa.

After reversing, the expression is converted to postfix form by using infix to postfix algorithm. After that again the postfix expression is 

reversed to get the prefix expression.




C. postfix to infix conversion

Step 1: Scan the expression from left to right.

For every symbol:

If it is an operand → push it onto the stack.
If it is an operator:
Pop the right operand.
Pop the left operand.

Create:

(left operator right)
Push the resulting expression back onto the stack.

At the end, the stack contains the complete infix expression.




D. prefix to infix conversion

Step 1: Scan from right to left

This is the main difference from postfix → infix.

For every symbol:

If it is an operand → push it onto the stack.
If it is an operator:
Pop the left operand.
Pop the right operand.

Create:

(left operator right)
Push the resulting expression back onto the stack.