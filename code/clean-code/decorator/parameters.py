from functools import wraps

def parameters(*args, **kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*fargs, **fkwargs):
            # Here you can manipulate args and kwargs if needed
            print(f"Parameters: args={args}, kwargs={kwargs}")
            return func(*fargs, **fkwargs)
        return wrapper
    return decorator

@parameters(1, 2, key='value')
def my_function(a, b, key=None):
    print(f"Function called with: a={a}, b={b}, key={key}")

if __name__ == "__main__":
    my_function(3, 4, key='another_value')
