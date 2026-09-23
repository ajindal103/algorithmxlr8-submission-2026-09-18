def main():
    rows, cols = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(rows)]

    # Write your solution here.
    # Print the next generation of the board (Conway's Game of Life
    # rules applied simultaneously): rows lines, each with cols
    # space-separated 0/1 values.

    # This function updates the board to the next state in Conway's Game of Life.
    # It first finds the number of rows and columns so it can scan every cell.
    # The direction list stores all 8 possible neighboring positions around a cell.
    # A separate next board is created so current updates do not affect neighbor counting.
    # For each cell, the code counts how many live neighbors it has from the original board.
    # A live cell stays alive only if it has 2 or 3 live neighbors.
    # A live cell dies if it has too few or too many live neighbors.
    # A dead cell becomes alive only if it has exactly 3 live neighbors.
    # After all next values are computed, they are copied back into the original board.
    # For the example shown, the board changes according to these rules and the updated board is returned.

    dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live = 0
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]

                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 1:
                    live += 1
            
            if board[i][j] == 0:
                result[i][j] = 1 if live == 3 else 0
            else:
                result[i][j] = 1 if live in (2, 3) else 0


    for i in range(rows):
        for j in range(cols):
            if j != cols-1:
                print(result[i][j], end = " ")
            else:
                print(result[i][j])

if __name__ == "__main__":
    main()
