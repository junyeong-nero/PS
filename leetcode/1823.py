class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a queue with friends numbered from 1 to n
        queue = deque(range(1, n + 1))

        # Iterate until only one friend remains
        while len(queue) > 1:
            # Rotate the queue so that the k-th friend comes to the front
            queue.rotate(-(k - 1))
            # Remove the k-th friend
            queue.popleft()

        # Return the remaining friend
        return queue[0]


# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:

#         # 2- > 4 -> 6(1) -> 3 -> 5

#         queue = list(range(1, n + 1))

#         def func(index):
#             new_index = index
#             temp = 0
#             while temp < k:
#                 new_index = (new_index + 1) % n
#                 if queue[new_index] > 0:
#                     temp += 1
#             return new_index

#         index = k - 1
#         for _ in range(n - 1):
#             queue[index] = -1
#             new_index = func(index)
#             index = new_index

#         return max(queue)
