def generator(limit):
    for i in range(2,limit+1):
        if i %2 ==0 :
            yield i  


# print(generator(10))
for i in generator(10):
    print(i)