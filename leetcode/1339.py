class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        def get_subtree_sum(node):
            if not node:
                return 0

            # 현재 노드 + 왼쪽 서브트리 합 + 오른쪽 서브트리 합
            current_sum = (
                node.val + get_subtree_sum(node.left) + get_subtree_sum(node.right)
            )
            subtree_sums.append(current_sum)
            return current_sum

        # 1. 전체 트리의 합 계산 및 모든 서브트리의 합 저장
        total_sum = get_subtree_sum(root)

        # 2. 최대 곱 계산 (정렬 불필요, 단순 순회로 해결)
        # 공식: (한쪽 서브트리의 합) * (나머지 합)
        max_prod = 0
        for s in subtree_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product

        # 3. 결과 반환
        MOD = 10**9 + 7
        return max_prod % MOD
