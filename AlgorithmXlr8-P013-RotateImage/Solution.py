def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # Write your solution here.
    # Print the matrix rotated 90 degrees clockwise: n lines, each with
    # n space-separated integers.

    def reverse(a, b, row):
        while (a < b):
            row[a], row[b] = row[b], row[a]
            a += 1
            b -= 1

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        reverse(0, n-1, matrix[i])

    for i in range(n):
        for j in range(n):
            if (j != n-1):
                print(matrix[i][j], end = " ")
            else:
                print(matrix[i][j])
            
if __name__ == "__main__":
    main()
