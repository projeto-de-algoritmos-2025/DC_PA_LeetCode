from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def combinations(n: int, k: int) -> int:
            if k > n:
                return 0
            if k == 0 or k == n:
                return 1
            numerator = 1
            denominator = 1
            for i in range(k):
                numerator *= (n - i)
                denominator *= (i + 1)
            return numerator // denominator

        def count_paths(subtree: List[int]) -> int:
            if len(subtree) <= 2:
                return 1

            root = subtree[0]
            left = [x for x in subtree[1:] if x < root]
            right = [x for x in subtree[1:] if x > root]
            left_paths = count_paths(left)
            right_paths = count_paths(right)
            total_combinations = combinations(len(left) + len(right), len(left))
            return total_combinations * left_paths * right_paths % MOD

        return (count_paths(nums) - 1) % MOD