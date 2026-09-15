# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def heapify(n: int, i:int):
#             largest = i
#             left = 2*i+1
#             right = 2*i+2

#             if left < n and nums[left] > nums[largest]: largest = left

#             if right < n and nums[right] > nums[largest]: largest = right

#             if largest != i: 
#                 nums[i], nums[largest] = nums[largest], nums[i]
#                 heapify(n, largest)

#         n = len(nums)

#         for i in range(n // 2-1, -1, -1):
#             heapify(n, i)

#         for i in range(n-1, 0, -1):
#             nums[0], nums[i] = nums[i], nums[0]
#             heapify(i,0)

#         return nums

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n // 2-1, -1, -1):
            self.heapify(nums,n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums,i,0)

        return nums

    def heapify(self, nums: list[int], n:int, i:int) -> None:
        while True:
            largest = i
            left = 2*i+1
            right = 2*i+2

            if left < n and nums[left] > nums[largest]: largest = left

            if right < n and nums[right] > nums[largest]: largest = right

            if largest == i: break
                
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest

        