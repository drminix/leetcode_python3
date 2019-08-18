class Solution:
    def isValid(self, s: str) -> bool:
        """Check if given string contains the valid parenthesis"""
        """Computational complexity: O(n) since we need to travese the given string once"""
        """Space complexity: O(n) as we push all opening brackets onto the stack"""

        # use a stack
        stack = []
        # dictioanry(hash-map) which holds the valid counter part
        valid_mapping = {"}": "{", "]": "[", ")": "("}

        # for every characters
        for char in s:
            # is it a closing bracket?
            if char in valid_mapping:
                # pop the topmost element
                top_element = stack.pop() if stack else '#'  # pop '#' if stack is empty
                # check if it's the matching pair
                if valid_mapping[char] != top_element:
                    return False
            else:  # it's opening bracket
                stack.append(char)

        # stack should be empty if valid
        return not stack  # empty stack = false
