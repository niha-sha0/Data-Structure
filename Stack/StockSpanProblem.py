Stock Span Problem:

I/P: N = 7, price[] = [100 80 60 70 60 75 85]

O/P: [1 1 1 2 1 4 6]

    def calculateSpan(self,price,n):
        stack = []
        res = []
        
        for i in range(n):
            while len(stack) > 0 and price[stack[-1]] <= price[i]:
                stack.pop()
            if not stack:
                res.append(i+1)
            else:
                res.append(i-stack[-1])
            
            stack.append(i)
        
        return res

Time Complexity: O(n)
Space Complexity: O(n)
