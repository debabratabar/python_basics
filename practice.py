import time

def cache(func):
    print("Start of decorater")
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print("result=" ,long_running_function(2, 3))
print("result2=" ,long_running_function(2, 3))
print(long_running_function(4, 3))