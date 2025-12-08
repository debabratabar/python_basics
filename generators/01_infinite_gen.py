def infinite_gen(name):
    cnt =1
    while True:
        yield f" {name}:= {cnt}"
        cnt+=1


def square_gen(n):
    for i in range(1,n+1):
        yield i*i


def fibo():
    a = 0 
    b = 1 
    while True:
        yield a
        a, b = b , a+b

def read_file():
    with open('practice.py' , 'r') as f :
        for line in f:
            yield line

def rollIwin(n):

    yield [n,n+1,n+2]


# gen2=rollIwin()


for i in range(1,11):
    print(next(rollIwin(i)))


# gen3 = read_file()
# for i in range(10):
#     print(next(gen3))

# arr=[]
# gen2 = fibo()
# for _ in range(10):
#     arr.append(next(gen2))

# print(arr)


# user1 = infinite_gen("usr1")
# user2 = infinite_gen("usr2")

# for _ in range(5):
#     print(next(user1))

# for _ in range(3):
#     print(next(user2))



# gen1 = square_gen(5)

# for val in gen1:
#     print(val)



