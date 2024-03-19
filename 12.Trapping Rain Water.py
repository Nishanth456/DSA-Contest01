class Solution:
    def trap(self, height: List[int]) -> int:
        count=0
        for i in range(1,len(height)-1):
            left=[]
            right=[]
            left=height[:i+1]
            right=height[i+1:]
            lmax=max(left)
            rmax=max(right)
            z=min(lmax,rmax)
            if z>height[i]:
                count+=z-height[i]
        return count