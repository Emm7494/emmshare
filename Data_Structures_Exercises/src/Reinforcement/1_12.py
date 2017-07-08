'''
Created on 8 Jul 2017
R-1.12 Python's random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
@author: Emma
'''
def randchoice(data):
    import random
    i = random.randrange(0, len(data), 1)
    
    return data[i]

if __name__ == '__main__':
    print(randchoice(data=[1, 2, 4, 8, 16, 32, 64, 128, 256]))