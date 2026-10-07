<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Maximum Sum Circular Subarray

**Difficulty:** `Medium`

## Problem

Given a circular integer array nums (the end connects back to the start), return the maximum possible sum of a non-empty subarray, where the subarray may wrap around from the end of the array back to the beginning.

Read n on the first line and the n integers on the second line of standard input. Print the maximum circular subarray sum to standard output.

## Examples

### Example 1

**Input**
```
4
1 -2 3 -2
```
**Output**
```
3
```

**Explanation:** The subarray [3] achieves the highest sum; wrapping doesn't improve on it.

### Example 2

**Input**
```
3
5 -3 5
```
**Output**
```
10
```

**Explanation:** Wrapping from the last 5 around to the first 5, excluding only -3, gives sum 10.

### Example 3

**Input**
```
3
-3 -2 -3
```
**Output**
```
-2
```

**Explanation:** Every element is negative, so the answer is the least negative single element, -2.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/maximum-sum-circular-subarray).