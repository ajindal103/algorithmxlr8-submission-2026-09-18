def main():
    m, n = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split())) if n > 0 else []

    # Write your solution here.
    # Print the merged sorted array (length m + n), space-separated.
    # nums1's first m entries are its real values; the trailing n entries
    # are placeholder zeros to be overwritten.

    i, j, k = m-1, n-1, m+n-1

    while (j >= 0):
        if (i >= 0 and nums1[i] > nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        
        k -= 1

    for num in nums1:
        print(num, end=" ")

    
        
        




if __name__ == "__main__":
    main()
