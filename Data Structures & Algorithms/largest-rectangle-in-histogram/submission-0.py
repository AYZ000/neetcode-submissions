class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights = heights + [0]

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                left_b = stack[-1] if stack else -1 
                width = i - left_b -1 

                max_area = max(max_area, height*width)
            
            stack.append(i)

        return max_area

if __name__ == "__main__":
    sol = Solution()

    heights = [7,1,7,2,2,4]
    print(sol.largestRectangleArea(heights))