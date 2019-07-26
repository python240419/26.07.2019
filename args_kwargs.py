
def foo(x, *args):
    print(f'x = {x}')
    print(type(args))
    for item in args:
        print(f'in args = {item}')
l = [1,2,3]
foo(3, 'hello', 'I' ,'Love','foo')

# targil - write sum method
sum(5, -6, 11.1, 12)


