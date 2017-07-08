'''
Created on 8 Jul 2017
R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
@author: Emma
'''
def plustwos(m, n, k):
    return [i for i in range(m, n, k)]

if __name__ == '__main__':
    print(plustwos(m=8, n=-10, k=-2))