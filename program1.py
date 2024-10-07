def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:  # It's a closing bracket
            # Pop the top element from the stack if it's not empty; otherwise, assign a dummy value '#'
            top_element = stack.pop() if stack else '#'

            # If the mapping for the current closing bracket doesn't match the stack's top element, return False
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, all the open brackets have been matched properly
    return not stack








    



  

