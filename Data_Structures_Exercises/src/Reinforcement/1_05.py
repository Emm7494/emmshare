'''
Created on 8 Jul 2017
R-1.5 Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.
@author: Emma
'''
def possum_2(n):
    assert n > 0
    return sum(i*i for i in range(1,n))

if __name__ == '__main__':
    print(possum_2(n=5))
