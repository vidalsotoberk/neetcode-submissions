class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        result = []

        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        while k > 0:
            best_freq = 0
            best_num = 0

            for num in count_map:
                if count_map[num] > best_freq:
                    best_num = num
                    best_freq = count_map[num]
            result.append(best_num)
            del count_map[best_num]
            k -= 1
        
        return result