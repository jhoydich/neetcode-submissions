class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        for l in s:
            if l in ["(", "[", "{"]:
                stack.append(l) 
            elif l in [")", "]", "}"]:
                try:
                    last = stack.pop()
                    if l == ")" and last == "(":
                        continue
                    if l == "]" and last == "[":
                        continue
                    if l == "}" and last == "{":
                        continue
                    return False
                except:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True