<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Substring with Concatenation of All Words

**Difficulty:** `Hard`

## Problem

Given a string s and an array of equal-length words, return all starting indices of substrings in s that are a concatenation of every word in words exactly once, in any order, with no extra characters in between.

Read s on the first line, the count of words on the second line, and the words (space-separated) on the third line of standard input. Print every matching starting index in ascending order, space-separated, on one line, or print "(none)" if there are no matches.

## Examples

### Example 1

**Input**
```
barfoothefoobarman
2
foo bar
```
**Output**
```
0 9
```

**Explanation:** "barfoo" at index 0 and "foobar" at index 9 both use each word exactly once.

### Example 2

**Input**
```
wordgoodgoodgoodbestword
4
word good best word
```
**Output**
```
(none)
```

**Explanation:** No substring provides two separate non-overlapping "word" chunks alongside "good", "good", "best".

### Example 3

**Input**
```
barfoofoobarthefoobarman
3
bar foo the
```
**Output**
```
6 9 12
```

**Explanation:** Indices 6, 9, and 12 each start a valid concatenation of all three words.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/substring-with-concatenation-of-all-words).