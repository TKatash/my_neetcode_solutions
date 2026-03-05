s = "([{}])"


def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []
    for i in s:
        if i in pairs:
            if stack and pairs[i] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not bool(stack)


print(isValid(s))
