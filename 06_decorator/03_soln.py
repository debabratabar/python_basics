import time 
from functools import wraps
def standard_func(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        print(time.ctime(time.time()))
        print(f'🚀 stating function run= {func.__name__}')
        func(*args , **kwargs)
        time.sleep(5)
        print(time.ctime(time.time()))
        print(f'✅ Ending function run= {func.__name__}')
    return wrapper

@standard_func
def write_word(str):
    print(str)

# write_word('Debabrata')
# print(write_word.__name__)


def cache_results(func):
    # Write your code below this line
    @wraps(func)
    def wrapper(a,b):
        cachee={}
        str = f"{a}*{b}"
        if str in cachee:
            print('From Cache: result')
            return cachee[str]
        else:
            print('Not From Cache: result')
            return func(a,b)

        
    return wrapper
        
    


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b


print(multiply(8,6))