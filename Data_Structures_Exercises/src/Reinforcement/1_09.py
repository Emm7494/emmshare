'''
Created on 8 Jul 2017
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
@author: Emma
'''
def plustens(m, n, k):
    return [i for i in range(m, n, k)]

if __name__ == '__main__':
    print(plustens(m=50, n=90, k=10))