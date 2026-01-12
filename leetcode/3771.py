class Solution:
    def totalScore(self, hp: int, dam: List[int], req: List[int]) -> int:

        # points at k starting from room i
        #  => hp - (damage from i to k) >= requirement[k]
        # re-arrange:
        #  => hp + (damage from k + 1 to n) - requirement[k] >= (damage from i to n)

        st = SortedList()
        res = cur = total = 0
        for d, r in list(zip(dam, req))[::-1]:
            st.add(hp + total - r)
            total += d
            res += len(st) - st.bisect_left(total)
        return res
