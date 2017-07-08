'''
Created on 8 Jul 2017
R-1.7 Give a single command that computes the sum from Exercise R-1.6,
relying on Python's comprehension syntax and the built-in sum function
@author: Emma
'''
def oddsum_2(n):
    assert n > 0
    return sum(i*i for i in range(1, n) if i & 1 )
    
if __name__ == '__main__':
    print(oddsum_2(n=5))