
def foo(x, *args):
    print(f'x = {x}')
    print(type(args))
    for item in args:
        print(f'in args = {item}')
l = [1,2,3]
foo(3, 'hello', 'I' ,'Love','foo')

# targil - write sum method
#my_sum(5, -6, 11.1, 12)
def my_sum(x, y, *args):
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

def statistics(k, **kwargs):
   print(f'keys = {kwargs.keys()}')
   print(f'values = {kwargs.values()}')
   if k in kwargs.keys():
       print(f'{k} in keys')
       return True
   if k in kwargs.values():
       print(f'{k} in values')
       return True
   print(list(kwargs.values()))
   print(list(kwargs.keys()))
   listOfAll =\
       list(kwargs.values())+\
       list(kwargs.keys())
   listComb = []
   for k,v in kwargs.items():
       listComb.append(k)
       listComb.append(v)

   return False

statistics('TV', name='danny',
    age=12, city='TV')

def foo3(x = 7, y = 9, **kwargs):
    pass
foo()
foo(y=8, a=1)


