from typing import List, Tuple

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[Tuple[int, int]]) -> List[int]:
        def get_kth_smallest_index(nums: List[str], k: int, trim_len: int) -> int:
            trimmed_with_index = [
                (num[-trim_len:], index)
                for index, num in enumerate(nums)
            ]
            trimmed_with_index.sort()
            return trimmed_with_index[k - 1][1]

        results: List[int] = []
        for kth, trim_length in queries:
            index = get_kth_smallest_index(nums, kth, trim_length)
            results.append(index)
        
        return results
