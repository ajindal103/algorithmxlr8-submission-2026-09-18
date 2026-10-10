def main():
    ransom_note = input().strip()
    magazine = input().strip()

    # Write your solution here.
    # Print "true" if ransom_note can be built using only letters available
    # in magazine (each letter of magazine usable at most once), else "false".

    freq = {}
    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1

    ans = True
    for ch in ransom_note:
        if freq.get(ch, 0) == 0:
            ans = False
        else:
            freq[ch] -= 1

    print("true") if ans else print("false")


if __name__ == "__main__":
    main()
