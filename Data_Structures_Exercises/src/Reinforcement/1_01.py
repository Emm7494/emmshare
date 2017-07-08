'''
Created on 8 Jul 2017
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
@author: Emma
'''
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(is_multiple(n=54, m=3))