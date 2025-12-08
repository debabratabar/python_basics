import time , math

def decorator(func):
    def wrapper1(*args , **kwargs):
        start_time =time.time()
        print(start_time)
        func(*args , **kwargs)
        end_time = time.time()
        print(end_time)
        print(math.floor( end_time - start_time))
    return wrapper1



@decorator
def long_running_func(seconds):
    print("Function Starts")
    time.sleep(seconds)
    print("Function ends")

@decorator
def print_my_name(name):
    print(f"My name is {name}")

long_running_func(5)
print_my_name("Debabrata Bar")