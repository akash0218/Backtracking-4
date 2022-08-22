# Time Complexity : exponential
# Space Complexity : O(h*w);
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#
#
import sys
from collections import deque


class Solution:
    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def bfs(self, grid, h, w):
        queue = deque()
        visited = []
        result = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for _ in range(h):
            visited.append([False]*w)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = True
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                pop = queue.popleft()
                for x in dirs:
                    nr = pop[0] + x[0]
                    nc = pop[1] + x[1]
                    if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == False:
                        grid[nr][nc] = level+self.distance(pop, [nr, nc])
                        result = max(grid[nr][nc], result)
                        queue.append([nr, nc])
                        visited[nr][nc] = True
            level += 1
        return result

    def backtrack(self, grid, r, c, h, w, n):
        # base
        if n == 0 or r == h:
            self.result = min(self.result, self.bfs(grid, h, w))
            return
        # logic
        for i in range(r, h):
            for j in range(c, w):
                # action
                grid[i][j] = 0
                if n != 0:
                    if j != w - 1:
                        self.backtrack(grid, r, c + 1, h, w, n - 1)
                    elif j == w - 1:
                        self.backtrack(grid, r + 1, 0, h, w, n - 1)
                # backtrack
                grid[i][j] = -1

    def OptimalBuildingPlacement(self, h, w, n):
        grid = []
        self.result = sys.maxsize
        for _ in range(h):
            grid.append([-1] * w)
        self.backtrack(grid, 0, 0, h, w, n)
        return self.result


print(Solution().OptimalBuildingPlacement(5, 5, 3))
