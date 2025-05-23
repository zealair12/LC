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
            elif abs(ast) >= last:      
                while last > 0 and abs(ast) > last and stk:
                    stk.pop()
                    if stk:
                        last = stk[-1]
                if last == abs(ast):
                    stk.pop()
                elif last < abs(ast):
                    stk.append(ast)

        return stk