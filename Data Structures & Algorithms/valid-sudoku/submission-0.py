class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        def getBox(row,col):
            if row < 3:
                if col < 3:
                    return 0
                if col < 6:
                    return 1
                else:
                    return 2
            elif row < 6:
                if col < 3:
                    return 3
                if col < 6:
                    return 4
                else:
                    return 5
            else:
                if col < 3:
                    return 6
                if col < 6:
                    return 7
                else:
                    return 8             


        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                box = getBox(row,col)

                if board[row][col] in rows[row]:
                    return False
                if board[row][col] in columns[col]:
                    return False
                if board[row][col] in boxes[box]:
                    return False

                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                boxes[box].add(board[row][col])
        
        return True