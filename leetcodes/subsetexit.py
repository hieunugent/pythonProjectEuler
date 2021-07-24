class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def backtracking(i, j, k, visited):
            if k == len(word):
                return True
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                _x = i + x
                _y = j + y
                if 0 <= _x < row and 0 <= _y < col and [_x, _y] not in visited and board[_x][_y] == word[k]:
                    visited.append([_x, _y])
                    if backtracking(_x, _y, k+1, visited):
                        return True
                    visited.remove([_x, _y])
            return False
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and backtracking(i, j, 1, [[i, j]]):
                    return True
        return False
