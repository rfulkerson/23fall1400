a = 200
b = 200 + 200
c = a + a 
d = b

# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

if d is c:
    print('d is c', end=' : ')
if d is b:
    print('d is b')
