from functools import wraps


class Parameters:
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*fargs, **fkwargs):
            # Here you can manipulate args and kwargs if needed
            print(f"Parameters: args={self.args}, kwargs={self.kwargs}")
            return func(*fargs, **fkwargs)
        return wrapper

@Parameters(1, 2, key='value')
def my_function(a, b, key=None):
    print(f"Function called with: a={a}, b={b}, key={key}")

if __name__ == "__main__":
    my_function(3, 4, key='another_value')