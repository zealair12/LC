class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []       

        for ast in asteroids:
            if not stk:
                stk.append(ast)
                continue
            last = stk[-1]
            if ast > 0 or last < 0: # key line to understand(takes care of most conditions)
                stk.append(ast) 
            elif last <= abs(ast):      
                while last > 0 and last < abs(ast) and stk:
                    stk.pop()
                    if stk:
                        last = stk[-1]
                if last == abs(ast):
                    stk.pop()
                elif last < abs(ast):
                    stk.append(ast)

        return stk