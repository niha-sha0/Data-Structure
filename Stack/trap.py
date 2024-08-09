Trapping Rain Water:

I/P: height = [0,1,0,2,1,0,1,3,2,1,2,1]
O/P: 6

Solution 1: 
  def trap(self, height):
        n = len(height)
        stack = []
        left = [0]*n
        right = [0]*n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        total = 0
        for i in range(n):
            leftMax = left[i]
            rightMax = right[i]

            total += min(leftMax, rightMax) - height[i]
        
        return total

T.C: O(n)
S.C: O(2n)

Solution 2:
  def trap(self, height):
        left, right, total = 0, 0, 0
        l = 0 
        r = len(height)-1
        
        while l < r:
            if height[l] <= height[r]:
                if left  > height[l]:
                    total += left - height[l]
                else:
                    left = height[l]
                l += 1
            else:
                if right > height[r]:
                    total += right - height[r]
                else:
                    right = height[r]
                r -= 1
                
        return total

T.C: O(n)
S.C: O(1)
