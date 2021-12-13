# Problem Statement for Different Characters
You are given a string S (ternary string) of length N, consisting of only 0s, 1s, and 2s.

#### Find the number of substrings of this string that start and end with different characters.
If the same substring appears multiple times in S, it is to be counted multiple times.

#### Note
A substring of a string is a contiguous subsequence of that string.

#### Input Format
The first line contains the integer N.
The second line contains the string S.

#### Constraints
1 <= N <= 104
S[i] = "0" or S[i] = "1" or or S[i] = "2"

#### Sample Input 1
5         -- denotes N
10201 -- denotes S

#### Output Format
The output returns the number of substrings of this string that start and end with different characters.

#### Sample Output 1
8

#### Explanation
The 8 substrings which start and end with different characters are shown below (highlighted):
a. 10201 → 10
b. 10201 → 02
c. 10201 → 102
d. 10201 → 20
e. 10201 → 1020
f. 10201 → 01
g. 10201 → 201
h. 10201 → 0201
Hence the output is 8.

#### Sample 2

##### Input
7
1111111

##### Output
0

#### Sample 3

##### Input
3
120

##### Output
3