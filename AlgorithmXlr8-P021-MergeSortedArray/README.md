<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Merge Sorted Array

**Difficulty:** `Easy`

## Problem

You are given two sorted integer arrays nums1 and nums2, with m and n elements respectively. nums1 has length m + n, where its first m entries are the actual sorted values and the remaining n entries are placeholder zeros. Merge nums2 into nums1 so that nums1 becomes one single sorted array of length m + n.

Read m and n on the first line of standard input, then nums1 (m + n integers) on the second line, then nums2 (n integers) on the third line. Print the merged sorted array, space-separated, to standard output.

## Examples

### Example 1

**Input**
```
3 3
1 2 3 0 0 0
2 5 6
```
**Output**
```
1 2 2 3 5 6
```

**Explanation:** Merging [1,2,3] and [2,5,6] gives [1,2,2,3,5,6].

### Example 2

**Input**
```
1 0
1

```
**Output**
```
1
```

**Explanation:** nums2 is empty, so nums1 stays as it is.

### Example 3

**Input**
```
0 1
0
1
```
**Output**
```
1
```

**Explanation:** nums1 has no real values, so the result is simply nums2.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/merge-sorted-array).