"""You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1"""
from collections import Counter
s = [input().strip() for _ in range(int(input()))]
print(len(Counter(s).keys()))
print(*Counter(s).values())