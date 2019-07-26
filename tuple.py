
# Tuple
def dontTouchMyList(l):
    l[0] = 10

l1 = [1,2,3,4]
#dontTouchMyList(tuple(l1)) # error
#print(l1)
#dontTouchMyList(l1.copy()) # less good
#l2 = l1.copy()
#l2[0] = 'ha ha ha'

# getUniqueTuple:
#  will get a list of numbers *args
#  return tuple from this list
#  contain only unique items
# getUniqueTuple(5, 5, 7, 9, 9, 8)
# *etgar return non-unique
#(7, 8)

def getUniqueTuple(*args):
    #return tuple([n for n in args\
    #      if args.count(n) == 1])
    res = []
    for n in args:
        if args.count(n) == 1:
            res.append(n)
    tup = tuple(res)
    return tup

def getNonUniqueTuple(*args):
    #return tuple([n for n in args\
    #      if args.count(n) == 1])
    res = []
    for n in args:
        if args.count(n) > 1:
            res.append(n)
    tup = tuple(res)
    return tup








