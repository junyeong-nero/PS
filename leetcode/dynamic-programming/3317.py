MOD = 10 ** 9 + 7
@cache
def s(n, k):
    if n < k: return 0
    if k == 1: return 1
    return (k * s(n - 1, k) + s(n - 1, k - 1)) % MOD

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        
        res = 0
        for a in range(1, min(n, x) + 1):
            # perm(x, a) : pick a stages 
            # s(n, a) : assign n performers to a events
            # pow(y, a) : each event can have score from 1 to y
            
            # why not combinations?
            #    - (1, 2, 3) / (3, 1, 2) is it different? : yes
            # performers 에 index 를 부여하거나 / stages 에 인덱스를 부여해야 different stages 
            # events를 구분할 수 있기 때문. 
            # 사용한 s(n, a) : stirling number 을 사용하는 경우, 그룹간의 구별이 사라짐
            # permutation 을 사용해야 다른 stage 라는 indexing 이 가능해진다.

            res += perm(x, a) * s(n, a) * pow(y, a, MOD)
            res %= MOD

        return res