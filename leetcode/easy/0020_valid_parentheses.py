def valid_parentheses(parentheses):
    stack=[]
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in parentheses:
        if ch in "([{":
            stack.append(ch)
        elif not stack:
            return False
        else:
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
            
    if not stack:
        return True
    else:
        return False

print(valid_parentheses("()"))       # True
print(valid_parentheses("([{}])"))   # True
print(valid_parentheses("([)]"))     # False
print(valid_parentheses("(("))       # False
print(valid_parentheses(")"))        # False