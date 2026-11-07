# 9:03
# Time: O(nlogn)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = dict()
        for num in nums:
          if num in count_map:
            count_map[num] += 1
          else:
            count_map[num] = 1

        count_map_array_sorted = sorted(count_map.items(), key=lambda count_map: count_map[1], reverse=True)

        return [count_map_array_sorted[i][0] for i in range(k)]
