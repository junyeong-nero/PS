from typing import List


class Solution:
    def lexicographicallySmallestArray(self, a: List[int], k: int) -> List[int]:
        """
        Rearranges the array 'a' to be lexicographically smallest by swapping elements
        within groups where the difference between consecutive elements' original values
        is less than or equal to 'k'.

        Args:
            a: The input list of integers.
            k: The maximum allowed difference for grouping elements.

        Returns:
            The lexicographically smallest array achievable through allowed swaps.
        """

        n = len(a)
        indexed_a = sorted(
            [(val, idx) for idx, val in enumerate(a)], key=lambda x: x[0]
        )

        groups = []
        current_group = [indexed_a[0]]

        for i in range(1, n):
            if indexed_a[i][0] - indexed_a[i - 1][0] <= k:
                current_group.append(indexed_a[i])
            else:
                groups.append(current_group)
                current_group = [indexed_a[i]]
        groups.append(current_group)

        for group in groups:
            indices = [idx for _, idx in group]
            indices.sort()
            for i, (val, _) in enumerate(group):
                a[indices[i]] = val

        return a
