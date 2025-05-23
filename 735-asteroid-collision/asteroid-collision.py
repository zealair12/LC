class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []       

        for ast in asteroids:
            if not stk:
                stk.append(ast)
                continue
            last = stk[-1]
            if ast > 0:
                stk.append(ast)
            elif ast * last > 0:
                stk.append(ast)
            elif abs(ast) == last:
                stk.pop()
            elif abs(ast) > last:
                stk.pop()
                if not stk or stk[-1] < 0:
                    stk.append(ast)
                else:   
                    last = stk[-1]     
                    while last > 0 and abs(ast) > last and stk:
                        stk.pop()
                        if stk:
                            last = stk[-1]
                    if last == abs(ast):
                        stk.pop()
                    elif last < abs(ast):
                        stk.append(ast)
                # 
                # while len(stk) > 1 and stk[-1] < 0 and stk[-2] > 0:
                #     if abs(stk[-1]) > stk[-2]:
                #         stk.pop(-2)
                #     elif abs(stk[-1]) < stk[-2]:
                #         stk.pop()
                #     else:
                #         stk.pop()
                #         stk.pop()
            

        return stk



