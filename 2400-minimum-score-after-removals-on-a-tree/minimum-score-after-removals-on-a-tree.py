import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        def dfs(node, parent):
            nonlocal time
            in_time[node] = time
            time += 1
            xor_val = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    xor_val ^= dfs(neighbor, node)
            subtree_xor[node] = xor_val
            out_time[node] = time
            time += 1
            return xor_val

        total_xor = dfs(0, -1)
        min_score = float('inf')

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        for i in range(1, n):
            for j in range(i + 1, n):
                if is_ancestor(i, j):  # j is in i's subtree
                    a, b, c = subtree_xor[j], subtree_xor[i] ^ subtree_xor[j], total_xor ^ subtree_xor[i]
                elif is_ancestor(j, i):  # i is in j's subtree
                    a, b, c = subtree_xor[i], subtree_xor[j] ^ subtree_xor[i], total_xor ^ subtree_xor[j]
                else:  # separate subtrees
                    a, b, c = subtree_xor[i], subtree_xor[j], total_xor ^ subtree_xor[i] ^ subtree_xor[j]

                min_score = min(min_score, max(a, b, c) - min(a, b, c))

        return min_score