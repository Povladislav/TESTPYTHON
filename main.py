
def decorator_function(funct_to_wrap):
    def wrapper():
        print("Yo!")
        funct_to_wrap()
    return wrapper()

@decorator_function
def my_func():
    print('Hello world!')
my_func()