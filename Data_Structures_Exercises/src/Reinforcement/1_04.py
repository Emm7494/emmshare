'''
Created on 8 Jul 2017
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
@author: Emma
'''
def possum_1(n):
    assert n > 0
    collect = (i*i for i in range(1, n) if i == abs(i))
    total = 0
    for j in collect:
        total += j
    
    return total
if __name__ == '__main__':
    print(possum_1(n=5))
