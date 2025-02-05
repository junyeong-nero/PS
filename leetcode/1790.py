class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff_indices = [i for i, (a, b) in enumerate(zip(s1, s2)) if a!= b]

        if len(diff_indices) == 0:  # Already handled by s1 == s2 check, but included for clarity
            return True
        elif len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        else:
            return False