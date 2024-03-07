# tuple1 = ("enna" , "meena" ,"tike")

# dict = {"key1" : "value1" , "key2":"value2"}

# my_str = ", ".join(tuple1)

# my_str_dict = ", ".join( f"{key}={value}" for key,value in dict.items())

# print(my_str)

# print(my_str_dict)

def decorator(func):
    def wrapper(*args , **kwargs):
        args_str = ", ".join(str(arg) for arg in args)
        print(f"Function Name ={func.__name__} and arguments are {args_str}")
        func(*args , **kwargs)
    return wrapper

@decorator
def hello(name , surname ):
    print(f"Hello {name} {surname}")


hello("Debabrata", "Bar")