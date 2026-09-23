class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set) # our columns is a hashmap where the key is a column and its value is a set
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                square = (col // 3, row // 3)

                if val == '.':
                    continue
                elif val in columns[col] or val in rows[row] or val in squares[square]:
                    return False
                columns[col].add(val)
                rows[row].add(val)
                squares[square].add(val)

        return True