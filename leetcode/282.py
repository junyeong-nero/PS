class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        # dfs(인덱스, 현재까지의 수식 문자열, 현재 계산된 값, 이전에 더해진 값)
        def dfs(index, path, value, last):
            # 문자열 끝에 도달했을 때
            if index == n:
                if value == target:
                    res.append(path)
                return

            # 현재 인덱스부터 끝까지 숫자를 하나씩 늘려가며 선택 (operand 선택)
            for i in range(index, n):
                # 선택한 숫자가 1자리 이상인데 '0'으로 시작하면 유효하지 않음 (예: "05")
                # 단, 숫자 "0" 자체는 허용
                if i > index and num[index] == "0":
                    break

                # 현재 선택한 숫자 부분 문자열
                curr_str = num[index : i + 1]
                curr_val = int(curr_str)

                # 식의 맨 처음에는 연산자가 붙지 않음
                if index == 0:
                    dfs(i + 1, curr_str, curr_val, curr_val)
                else:
                    # 1. 덧셈 (+)
                    dfs(i + 1, path + "+" + curr_str, value + curr_val, curr_val)

                    # 2. 뺄셈 (-)
                    dfs(i + 1, path + "-" + curr_str, value - curr_val, -curr_val)

                    # 3. 곱셈 (*)
                    # 곱셈은 우선순위가 높으므로, 직전에 더했던 값(last)을 빼고
                    # (last * curr_val)을 다시 더해줘야 함
                    # 예: 2 + 3 * 4  =>  (5 - 3) + (3 * 4) = 2 + 12 = 14
                    dfs(
                        i + 1,
                        path + "*" + curr_str,
                        value - last + (last * curr_val),
                        last * curr_val,
                    )

        dfs(0, "", 0, 0)
        return res
