"""
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise,
print False.
In the second line, print True if S has any alphabetical characters. Otherwise,
print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise,
print False.
In the fifth line, print True if S has any uppercase characters. Otherwise,
print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""

if __name__ == '__main__':
    s = input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
