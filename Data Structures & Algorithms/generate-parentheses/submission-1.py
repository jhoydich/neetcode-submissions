class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        self.parentheses = []

        self.DFSString("", n*2, True)

        return self.parentheses
    
    def validate(self, par: str):
        op = 0

        for s in par:
            if s == "(":
                op += 1
            else:
                op -= 1
            if op < 0:
                return
        if op == 0:
            self.parentheses.append(par)
        
    def DFSString(self, par_str: str, length: int, left: bool):
        if left:
            par_str += "("
        else:
            par_str += ")"
        
        if len(par_str) == length:
            self.validate(par_str)
            return
        
        # build left strings
        self.DFSString(par_str, length, True)

        # build right strings
        self.DFSString(par_str, length, False)


        