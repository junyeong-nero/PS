class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        def time2int(s):
            return int(s[:2]) * 60 + int(s[2:])

        history = defaultdict(list)
        for name, time in access_times:
            history[name].append(time2int(time))

        def check_accesses(arr):
            arr = sorted(arr)
            n = len(arr)
            i, j = 0, 0
            res = 0
            while i <= j < n:
                if arr[j] - arr[i] < 60:
                    j += 1
                    res = max(res, j - i)
                else:
                    i += 1

            return res >= 3

        # print(history)

        res = []
        for name, accesses in history.items():
            if check_accesses(accesses):
                res.append(name)

        return res
