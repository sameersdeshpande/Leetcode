class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove= set()
        stack =[]

        for i , c in enumerate(s):
            if c=="(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        to_remove.update(stack)

        res = []
        for i,c in enumerate(s):
            if i not in to_remove:
                res.append(c)
        return ''.join(res)

                    



        