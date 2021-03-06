def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield a
        a,b = b,a+b
    return

for item in fib(10):
    print(item)

# a,b = 0,1
# for i in range(10):
#     print(a)
#     a,b = b,a+b
