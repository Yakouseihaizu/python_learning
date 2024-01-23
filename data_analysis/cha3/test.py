# def func():
#     a = []
#     for i in range(5):
#         a.append(i)
# func()
# print(a)

# a = []
# def func():
#     # a = [1]
#     for i in range(5):
#         a.append(i)
# func()
# print(a)

# a = None

# def func():
#     global a
#     a = []
#     for i in range(5):
#         a.append(i)

# func()
# print(a)

# def f():
#     a = 5
#     b = 6
#     c = 7
#     return a,b,c

# a,b,c = f()
# print(a,b,c)

# def short_function(x):
#     return x*2

# equiv_anon = lambda x:x*2
# print(equiv_anon(2))
# print(short_function(2))

# def apply_to_list(some_list,f):
#     return [f(x) for x in some_list]
# inits = [4,0,1,5,3]
# apply_to_list(inits,lambda x:x*2)

def sqaure(n=10):
    print('Generating squares form 1 to {0}'.format(n**2))
    for i in range(1,n+1):
        u = 1
        yield i**2

gen = sqaure()
for i in gen:
    print(i,end=' ')

