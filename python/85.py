# Program 157: Valid Parentheses

def is_valid(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


text = input("Enter brackets: ")

if is_valid(text):
    print("Valid parentheses")
else:
    print("Invalid parentheses")