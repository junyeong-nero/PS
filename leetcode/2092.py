from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # Set of people who know the secret
        known = {0, firstPerson}

        # Group meetings by time and process
        i = 0
        m = len(meetings)
        while i < m:
            j = i
            time = meetings[i][2]

            # Identify the range of meetings with the same time
            while j < m and meetings[j][2] == time:
                j += 1

            # meetings[i:j] are all happening at 'time'
            current_batch = meetings[i:j]

            # Build graph for this batch
            adj = defaultdict(list)
            people_in_batch = set()

            for u, v, w in current_batch:
                adj[u].append(v)
                adj[v].append(u)
                people_in_batch.add(u)
                people_in_batch.add(v)

            # Find starting points for BFS (people who already know the secret)
            queue = deque()
            for p in people_in_batch:
                if p in known:
                    queue.append(p)

            # BFS to propagate secret within this time group
            visited = set(queue)
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
                        visited.add(neighbor)

            i = j  # Move to next batch

        return sorted(list(known))
