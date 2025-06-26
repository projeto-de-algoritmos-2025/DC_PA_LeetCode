from typing import List, Tuple

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[Tuple[int, int]]) -> List[int]:
        
        def merge_sort(arr: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left: List[Tuple[str, int]], right: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and left[i][1] < right[j][1]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def get_kth_smallest_index(nums: List[str], k: int, trim_len: int) -> int:
            trimmed_with_index = [
                (num[-trim_len:], index)
                for index, num in enumerate(nums)
            ]
            sorted_trimmed = merge_sort(trimmed_with_index)
            return sorted_trimmed[k - 1][1]

        results: List[int] = []
        for kth, trim_length in queries:
            index = get_kth_smallest_index(nums, kth, trim_length)
            results.append(index)

        return results

