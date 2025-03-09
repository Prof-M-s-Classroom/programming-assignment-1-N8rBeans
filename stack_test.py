from stack import CircularStack

stack = CircularStack(1)
stack.print_stack()

stack.push(2)
stack.print_stack()
stack.push(3)
stack.print_stack()
stack.push(4)
stack.print_stack()
stack.push(5)
stack.print_stack()

stack.push(6)
stack.print_stack()
stack.push(7)
stack.print_stack()
stack.push(8)
stack.print_stack()

print()
print(stack.is_empty())

print()
print(stack.peek().data)

print()
print(stack.pop().data)
stack.print_stack()
print()
print(stack.pop().data)
stack.print_stack()
print()
print(stack.pop().data)
stack.print_stack()
print()
print(stack.pop().data)
stack.print_stack()
print()
print(stack.pop().data)
stack.print_stack()

print(stack.is_empty())

stack.push(1)
stack.print_stack()
print(stack.is_empty())
