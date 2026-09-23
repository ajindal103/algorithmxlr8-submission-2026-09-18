def main():
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]

    # Write your solution here.
    # Print every element of matrix in spiral order, space-separated on one line.

    rs, re, cs, ce = 0, m-1, 0, n-1

    total = m*n
    count = 0
    while (count < total):
        for i in range(cs, ce+1):
            if (count < total):
                count += 1
                print(matrix[rs][i], end=" ")
        rs += 1
        
        for i in range(rs, re+1):
            if (count < total):
                count += 1
                print(matrix[i][ce], end=" ")
        ce -= 1
        
        for i in range(ce, cs-1, -1):
            if (count < total):
                count += 1
                print(matrix[re][i], end=" ")
        re -= 1
        
        for i in range(re, rs-1, -1):
            if (count < total):
                count += 1
                print(matrix[i][cs], end=" ")
        cs += 1        

if __name__ == "__main__":
    main()
