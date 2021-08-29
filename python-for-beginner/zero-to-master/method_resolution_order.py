# MRO - Method Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())
print(D.__str__)

class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass
print(M.mro())

"""
First, the interpreter scans M. Then, it scans B, and then A-B first because of the order of arguments at the time of inheritance.

It scans Z later, after X and Y. The order is- X, then Y, then Z. This is because due to depth-first search, X comes first to A.

Finally, it scans the class object. Hence, the order.
"""