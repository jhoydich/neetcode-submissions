class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        freq_count = {}
        freq_list = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq_count[n] = 1 + freq_count.get(n, 0)
        
        for n, count in freq_count.items():
            freq_list[count].append(n)
        
        top_k = []
        for i in range(len(freq_list) -1, -1, -1):
            for num in freq_list[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

        return top_k