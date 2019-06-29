def gen():
    try:
        yield 1
    except ValueError as e:
        print("got ValueError from upstream!", repr(e.args))
    yield "str1"
    raise TypeError

def gen2():
    print((yield from gen()))

g = gen2()
print(next(g))
print(g.throw(ValueError))
try:
    print(next(g))
except TypeError:
    print("got TypeError from downstream!")

# passing None as second argument to throw
g = gen2()
print(next(g))
print(g.throw(ValueError, None))
try:
    print(next(g))
except TypeError:
    print("got TypeError from downstream!")

# passing an exception instance as second argument to throw
g = gen2()
print(next(g))
print(g.throw(ValueError, ValueError(123)))
try:
    print(next(g))
except TypeError:
    print("got TypeError from downstream!")
