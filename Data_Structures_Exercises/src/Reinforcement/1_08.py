'''
Created on 8 Jul 2017
R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index k in [-n,0),
what is the equivalent index non-negative j such that s[j] references
the same element?
@author: Emma
'''
def indexing(data):
    couple = [(i, -(i+1)) for i in range(-len(data), 0)]
    
    return couple
if __name__ == '__main__':
    print(indexing(data=[9, 7, 4, 8, 2, 6, 1, 2, 0, 3]))
    print('''                                                ***My Answer***\n
The sum of the value of the forward-index and it's equivalent backward-index should always be equal to -1.
Hence, the equivalent index, non-negative j such that s[j] references the same element is: j=-(k+1), for k in (infinity, -1].''')