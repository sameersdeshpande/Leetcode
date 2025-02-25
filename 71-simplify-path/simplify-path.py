class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for component in components:
            if component =='..':
                if stack:
                    stack.pop()
            elif component == "." or not component:
                continue
            else:
                stack.append(component)
        simplified_path = '/'+ '/'.join(stack)

        return simplified_path if stack else '/'
                
        