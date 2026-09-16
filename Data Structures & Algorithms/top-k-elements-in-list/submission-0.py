class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        freq = [[]for _ in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    sol = Solution()

nums = [1,2,2,3,3,3]
k = 2

print(sol.topKFrequent(nums, k))