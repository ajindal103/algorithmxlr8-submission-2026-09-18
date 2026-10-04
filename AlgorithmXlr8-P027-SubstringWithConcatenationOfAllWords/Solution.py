def main():
    s = input().strip()
    num_words = int(input())
    words = input().split()

    # Write your solution here.
    # Print every starting index (space-separated, ascending order) where a
    # substring of s is an exact concatenation of every word in words used
    # exactly once, in any order. If there are none, print "(none)".

    n = len(s)
    word_len = len(words[0])
    need = {}
    for w in words:
        need[w] = need.get(w, 0) + 1

    result = []
    for offset in range(word_len):
        left = offset
        count = 0
        window = {}
        right = offset
        while right + word_len <= n:
            piece = s[right : right+word_len]

            if piece in need:
                count += 1
                window[piece] = window.get(piece, 0) + 1

                while window[piece] > need[piece]:
                    left_piece = s[left : left+word_len]
                    window[left_piece] -= 1
                    left += word_len
                    count -= 1

                if count == num_words:
                    result.append(left)
                    left_piece = s[left : left+word_len]
                    window[left_piece] -= 1
                    left += word_len
                    count -= 1
            
            else:
                window.clear()
                count = 0
                left = right + word_len

            
            right += word_len      

    if result:
        for i in result:
            print(i, end=" ") 
    else:
        print("(none)")


if __name__ == "__main__":
    main()

# Calculate the length of each word and the total number of words.
# Store the required frequency of every word.
# Try every possible starting alignment based on the word length.
# For each alignment, initialize the sliding window from the left.
# Take one word-sized piece at a time from the string.
# If the piece is required, add it to the current window.
# If a word appears too many times, move the left boundary forward by one word.
# When the window contains all required words, record its starting position.
# After recording, remove the leftmost word so the search can continue.
# If the piece is not required, reset the window and start after that piece.