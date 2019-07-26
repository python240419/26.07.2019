
def foo(x, *args):
    print(f'x = {x}')
    print(type(args))
    for item in args:
        print(f'in args = {item}')
l = [1,2,3]
foo(3, 'hello', 'I' ,'Love','foo')

# targil - write sum method
#my_sum(5, -6, 11.1, 12)
def my_sum(*args):
    sum = 0
    for n in args:
        sum = sum + n # or: sum += n
    return sum
print(my_sum(6, 77, -5, 99.7))
print(my_sum())

# to_list - etgar
#print(to_list(1,2,3)) # [1,2,3]

# difference between list - we
# can avoid sending at all
#def foo2(*args):
#    pass
#foo2(  )

# **kwargs
# like *args - accepts dictionary
def printDictionary(**kwargs):
    for k, v in kwargs.items():
        print(f'key: {k} value: {v}')
printDictionary()
printDictionary(name='danny',
                age=12,
                city='TV')
# statistics(k, **kwargs)
# print - keys, values
#  return- does k appear in dict?
# *etgar - return a list from kwargs




