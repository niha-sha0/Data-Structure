Next Greater Element to Right:

I/P: arr[] = [6 8 0 1 3], n = 5
O/P: [8 -1 1 3 -1]

    def nextLargerElement(self,arr,n):
        stack = []
        res = [-1]*n
        
        for i in range(n-1, -1, -1):
            while(len(stack) > 0 and stack[-1] <= arr[i]):
                stack.pop()
            if stack:
                res[i] = stack[-1]
            
            stack.append(arr[i])
        
        return res

Time Complexity: O(n)
Space Complexity: O(n)
