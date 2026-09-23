<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Game of Life

**Difficulty:** `Medium`

## Problem

Given an m x n binary grid board representing Conway's Game of Life, compute the next state of every cell simultaneously: a live cell (1) with fewer than 2 or more than 3 live neighbors dies; a live cell with 2 or 3 live neighbors survives; a dead cell (0) with exactly 3 live neighbors becomes alive. Update the board in place.

Read rows and cols on the first line, followed by rows lines each with cols space-separated 0/1 values, on standard input. Print the next generation: rows lines, each with cols space-separated values.

## Examples

### Example 1

**Input**
```
4 3
0 1 0
0 0 1
1 1 1
0 0 0
```
**Output**
```
0 0 0
1 0 1
0 1 1
0 1 0
```

**Explanation:** Every cell's next state is computed from its 8 neighbors in the current generation.

### Example 2

**Input**
```
2 2
1 1
1 0
```
**Output**
```
1 1
1 1
```

**Explanation:** The single dead cell has exactly 3 live neighbors and becomes alive.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/game-of-life).