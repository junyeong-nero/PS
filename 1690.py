from typing import List
from functools import lru_cache

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Calculates the maximum score difference between Alice and Bob in the Stone Game VII using DFS with memoization.

        Args:
            stones: A list of integers representing the values of the stones.

        Returns:
            The maximum score difference between Alice and Bob if they both play optimally.
        """
        n = len(stones)
        
        @lru_cache(None)
        def dfs(left: int, right: int, turn: bool) -> int:
            """
            Depth-first search to explore all game states.
            
            Args:
                left: The left index of the current subarray.
                right: The right index of the current subarray.
                turn: True if it's Alice's turn, False if it's Bob's turn.

            Returns:
                The maximum score difference achievable from the current game state.
            """
            if left > right:
                return 0  # Base case: No stones left
            
            score_left = sum(stones[left+1 : right+1])
            score_right = sum(stones[left: right])
                
            if turn:  # Alice's turn (Maximize score difference)
                return max(score_left + dfs(left + 1, right, False), 
                           score_right + dfs(left, right - 1, False))
            else:  # Bob's turn (Minimize score difference)
                 return min(-score_left + dfs(left + 1, right, True), 
                            -score_right + dfs(left, right - 1, True))
        
        return dfs(0, n - 1, True)