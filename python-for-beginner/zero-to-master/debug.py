"""
step
a -> print out all variables in that steps

we can change the variable at runtime with pdb
"""
import pdb

def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, 'abcdef')