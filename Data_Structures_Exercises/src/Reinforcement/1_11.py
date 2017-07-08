'''
Created on 8 Jul 2017
R-1.11 Demonstrate how to use Python's list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
@author: Emma
'''
def squares(data=[1, 2, 4, 8, 16, 32, 64, 128, 256]):
    return [2**i for i in range(len(data)) ]

if __name__ == '__main__':
    print(squares())