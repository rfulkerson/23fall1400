def do_it(thing):
    return thing * 4

print(do_it(5))
print(do_it("hello"))
print(do_it(3.5))
print(do_it([2,3,4]))

x = 5
print(type(x),x)
x *= 3.5
print(type(x),x)
x = "hello"
print(type(x),x)