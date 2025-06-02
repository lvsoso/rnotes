from functools import wraps

def decorator(function=None, *, x=1, y=2):
    if function is None: # called as '@decorator(...)'

        def decorated(function):
            @wraps(function)
            def wrapped():
                return function(x, y)

            return wrapped

        return decorated
    else: # called as '@decorator'

        @wraps(function)
        def wrapped():
            return function(x, y)

        return wrapped

