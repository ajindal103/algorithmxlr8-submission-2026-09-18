def main():
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]

    # Write your solution here.
    # Print the matrix after zeroing out the entire row and column of
    # every original zero: rows lines, each with cols space-separated
    # integers.

    col = 1

    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == 0):
                if (j==0): col = 0
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            matrix[i][j] = 0 if 0 in (matrix[0][j], matrix[i][0]) else matrix[i][j]

    if col==0:
        for i in range(rows):
            matrix[i][0] = 0

    for i in range(rows):
        for j in range(cols):
            if (j==cols-1):
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=" ")


if __name__ == "__main__":
    main()
