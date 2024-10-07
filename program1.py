def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:  # It's a closing bracket
           
            top_element = stack.pop() if stack else '#'

            
            if bracket_map[char] != top_element:
                return False
        else:
           
            stack.append(char)

   
    return not stack








    



  

