# QUESTION 7
def prefix_to_infix(prefix):
    stack = []
    for char in reversed(prefix):
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = f"({operand1}{char}{operand2})"
            stack.append(expression)
    return stack.pop()

prefix = input("Enter prefix expression: ")
infix = prefix_to_infix(prefix)
print("Infix expression:", infix)



# QUESTION 8

def is_balanced(code):
    stack = []
    for char in code:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack

code = input("Enter a code snippet: ")
if is_balanced(code):
    print("All brackets are closed.")
else:
    print("Not all brackets are closed.")

