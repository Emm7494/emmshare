'''
Created on 8 Jul 2017
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
@author: Emma
'''
def minmax(data):
    max_i = min_i = data[0]
    
    for i in range(len(data)):
        
        if data[i] > max_i:
            max_i = data[i]
        elif data[i] < min_i:
            min_i = data[i]
        else:
            continue
    
    return min_i,max_i

if __name__=='__main__':
    print(minmax(data=[9, 7, 4, 8, 2, 6, 1, 2, 0, 3]))