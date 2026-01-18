class Solution:
    def earliestFullBloom(self, p_arr: List[int], g_arr: List[int]) -> int:
        # plantTime과 growTime을 묶어서 리스트로 만듭니다.
        # growTime이 긴 순서대로(내림차순) 정렬합니다.
        # growTime이 같다면 plantTime은 순서 상관 없습니다.
        jobs = sorted(zip(p_arr, g_arr), key=lambda x: -x[1])

        current_plant_time = 0
        max_bloom_time = 0

        for p, g in jobs:
            # 1. 현재 꽃을 심는 데 걸리는 시간을 누적합니다. (순차적)
            current_plant_time += p

            # 2. 현재 꽃이 다 피는 시간은 (심기 완료 시점 + 자라는 시간)입니다.
            bloom_time = current_plant_time + g

            # 3. 전체 꽃이 다 피는 시간은, 개별 꽃들이 피는 시간 중 가장 늦은 시간입니다.
            max_bloom_time = max(max_bloom_time, bloom_time)

        return max_bloom_time
