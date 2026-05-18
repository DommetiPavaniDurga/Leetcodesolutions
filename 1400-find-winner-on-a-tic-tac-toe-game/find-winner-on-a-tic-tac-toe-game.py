from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # initialize rows, cols and diagonals
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0

        # player A = +1, B = -1
        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == 2:
                anti_diag += player

            # check if current player wins
            if (abs(rows[r]) == 3 or 
                abs(cols[c]) == 3 or 
                abs(diag) == 3 or 
                abs(anti_diag) == 3):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == 9 else "Pending"
