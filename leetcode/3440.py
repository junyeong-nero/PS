class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:

        startTime += [eventTime]
        endTime += [eventTime]

        n = len(startTime)
        last = 0

        blanks = []
        removable = [False] * n

        for i in range(n):
            start, end = startTime[i], endTime[i]
            blanks.append(start - last)
            last = end

        print(blanks)
        # blanks[i] : i-th block 이전의 공백 크기

        for i in range(n):
            start, end = startTime[i], endTime[i]
            block_size = end - start
            for j in range(n):
                if i <= j <= i + 1:
                    continue
                if blanks[j] >= block_size:
                    removable[i] = True
                    break
        print(removable)

        res = 0
        for i in range(n - 1):
            start, end = startTime[i], endTime[i]
            temp = blanks[i] + blanks[i + 1] + ((end - start) if removable[i] else 0)
            res = max(res, temp)

        return res
