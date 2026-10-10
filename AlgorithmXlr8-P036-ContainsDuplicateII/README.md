<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Contains Duplicate II

**Difficulty:** `Easy`

## Problem

Given an integer array nums and an integer k, return true if there exist two distinct indices i and j such that nums[i] equals nums[j] and the absolute difference between i and j is at most k.

Read n and k on the first line of standard input, then n space-separated integers on the second line. Print true or false to standard output.

## Examples

### Example 1

**Input**
```
4 3
1 2 3 1
```
**Output**
```
true
```

**Explanation:** The two 1's are at indices 0 and 3, a distance of 3, which is within k.

### Example 2

**Input**
```
4 1
1 0 1 1
```
**Output**
```
true
```

**Explanation:** The 1's at indices 2 and 3 are a distance of 1 apart, within k.

### Example 3

**Input**
```
6 2
1 2 3 1 2 3
```
**Output**
```
false
```

**Explanation:** Every repeated value is more than 2 indices away from its previous occurrence.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/contains-duplicate-ii).