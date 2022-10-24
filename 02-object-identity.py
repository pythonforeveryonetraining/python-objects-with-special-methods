a1 = 10  # immutable type int
a2 = 10
print(a1 is a2)  # True

b1 = 4254543525425410  # immutable type int
b2 = 4254543525425410
print(b1 is b2)  # True

l1 = []  # mutable type list
l2 = []
print(l1 is l2)  # False

s1 = "HelloHelloHello"  # immutable type string
s2 = "HelloHelloHello"
print(s1 is s2)  # True

t1 = "Hello" * 3
t2 = "Hello" * 3
print(t1 is t2)  # True

x = 3
u1 = "Hello" * x
u2 = "Hello" * x
print(u1 is u2)  # False
