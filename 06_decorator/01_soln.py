import time , math

def decorator(func):
    def wrapper(*args , **kwargs):
        start_time =time.time()
        func(*args , **kwargs)
        end_time = time.time()
        print(math.floor( end_time - start_time))
    return wrapper



@decorator
def long_running_func(seconds):
    print("Function Starts")
    time.sleep(seconds)
    print("Function ends")

long_running_func(5)