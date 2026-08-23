class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getBox(r, c):
            x = r // 3
            y = c // 3

            return (x,y)


        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                b = getBox(r,c)    
                
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[b]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)
        
        return True