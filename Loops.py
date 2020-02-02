Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, 

Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16

#Code

ns = int(input())
n=int(ns)
for i in range(n):
    print(i*i)
