Longest Valid Parenthesis:

I/P: S = )()())
O/P: 4

  def maxLength(self, S):
        stack = []
        stack.append(-1)
        res = 0
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res

Time Complexity: O(n)
Space Complexity: O(n)
