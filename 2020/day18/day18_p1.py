with open('input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def eval(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2

# sample: 6
def simplify(expr):
    while len(expr) > 1:
        num1 = int(expr.pop())
        op = expr.pop()
        num2 = int(expr.pop())
        result = eval(num1, num2, op)
        expr.append(str(result))

    return expr[0]

total = 0
for line in data:
    line = line.replace('(', '( ')
    line = line.replace(')', ' )')
    expr = line.split()

    stack = []

    # expr (list): 3+4*(1*2)
    # stack (stack): 2*4+3
    # ordered: 2
    for ch in expr:
        if ch.isdigit() or ch in ['*', '+', '(']:
            stack.append(ch)

        elif ch == ')':
            ordered = []
            while stack[len(stack) - 1] != '(':
                ordered.append(stack.pop())
            stack.pop()

            result = simplify(ordered)
            stack.append(result)

    stack.reverse()


    result = simplify(stack)

    total += int(result)

print(total)
