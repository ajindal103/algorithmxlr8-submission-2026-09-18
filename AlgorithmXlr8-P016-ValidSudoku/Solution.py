def main():
    board = [input().strip() for _ in range(9)]

    # Write your solution here.
    # Print "true" if the board satisfies Sudoku's row/column/box
    # uniqueness rules among filled cells, otherwise print "false".

    # This function checks whether a Sudoku board follows the rules so far.
    # It keeps one set for each row, one set for each column, and one set for each 3x3 box.
    # A set is useful because it can quickly tell whether a digit has already appeared.
    # The function scans every cell in the 9 by 9 board one by one.
    # If a cell contains a dot, it means the cell is empty, so it is ignored.
    # For each filled cell, the function works out which 3x3 box that cell belongs to.
    # It then checks whether that digit is already present in the same row, column, or box.
    # If the digit is found again in any of those places, the board is invalid.
    # If not, the digit is added to the matching row, column, and box sets.
    # If the entire board is checked without any conflict, the function returns True.

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    def check():
        for i in range(9):
            for j in range(9):
                c = board[i][j]

                if (c == '.'):
                    continue
                
                box_index = (i // 3) * 3 + (j // 3)

                if c in rows[i] or c in cols[j] or c in boxes[box_index]:
                    return False

                rows[i].add(c)
                cols[j].add(c)
                boxes[box_index].add(c)

        return True 

    print("true") if check() else print("false")


if __name__ == "__main__":
    main()
