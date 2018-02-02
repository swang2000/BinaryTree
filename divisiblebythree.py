'''
Number of Groups of Sizes Two Or Three Divisible By 3
3.3
You are given N distinct numbers. You are tasked with finding the number of groups of 2 or 3 that can be formed whose sum is divisible by three.

Examples:

Input  : 1 5 7 2 9 14
Output : 13
The groups of two that can be
formed are:
(1, 5)
(5, 7)
(1, 2)
(2, 7)
(1, 14)
(7, 14)
The groups of three are:
(1, 5, 9)
(5, 7, 9)
(1, 2, 9)
(2, 7, 9)
(2, 5, 14)
(1, 9, 14)
(7, 9, 14)

Input  : 3 6 9 12
Output : 10
All groups of 2 and 3 are valid.
'''


def divisibleby3(a):
    count2 = 0
    count3 = 0
    for i in a:
        b = a.copy()
        b.remove(i)
        for j in b:
            if (i + j)%3 == 0:
                count2 += 1
            c = b.copy()
            c.remove(j)
            for k in c:
                if (i+j+k) % 3 ==0:
                    count3 +=1
    return count2/2 + count3/6

a= [1, 5, 7, 2, 9, 14]
b = [3, 6, 9, 12]
c = divisibleby3(b)

