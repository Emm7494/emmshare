'''
Created on 8 Jul 2017
R-1.2 Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
@author: Emma
'''
def is_even(k):
    if not k & 1:
        return True
    else:
        return False
    
if __name__=='__main__':
    print(is_even(k=20))

