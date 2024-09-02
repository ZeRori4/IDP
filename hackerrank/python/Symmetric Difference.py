"""
Given  sets of integers,  and , print their symmetric difference in ascending
order. The term symmetric difference indicates those values that exist in either
  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
"""


def symmetric_difference(m, a, n, b):
    set_a = set(a)
    set_b = set(b)
    diff = set_a.symmetric_difference(set_b)
    result = sorted(list(diff))
    for num in result:
        print(num)


m = int(input())
a = [int(x) for x in input().split()]
n = int(input())
b = [int(x) for x in input().split()]

symmetric_difference(m, a, n, b)
