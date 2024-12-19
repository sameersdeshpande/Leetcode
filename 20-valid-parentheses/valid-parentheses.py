class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping for matching brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Traverse each character in the string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:  # Check for matching opening bracket
                    return False
            else:  # If it's an opening bracket
                stack.append(char)
        
        # If stack is empty, all brackets matched properly
        return not stack
