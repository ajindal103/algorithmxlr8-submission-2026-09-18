<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Valid Sudoku

**Difficulty:** `Medium`

## Problem

Given a 9x9 Sudoku board (partially filled), determine if it is valid: only the filled cells (digits '1'-'9') need to be validated, and each row, each column, and each of the nine 3x3 sub-boxes must contain no repeated digit. Empty cells are represented by '.'.

Read 9 lines of standard input, each a 9-character string representing one row of the board. Print "true" if the board is valid, otherwise print "false".

## Examples

### Example 1

**Input**
```
53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
```
**Output**
```
true
```

**Explanation:** No row, column, or box has a repeated digit among its filled cells.

### Example 2

**Input**
```
83..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
```
**Output**
```
false
```

**Explanation:** Placing an 8 at row 0, column 0 duplicates the 8 already present in column 0's box, making the board invalid.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/valid-sudoku).