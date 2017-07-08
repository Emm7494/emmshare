'''
Created on 8 Jul 2017
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
@author: Emma
'''
def sumodd_1(n):
    assert n > 0
    collect = (i*i for i in range(1, n) if i & 1)
    total = 0
    
    for j in collect:
        total += j
    
    return total

if __name__ == '__main__':
    print(sumodd_1(n=5))