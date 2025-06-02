import contextlib

@contextlib.contextmanager
def db_handler():
    try:
        print("Opening database connection")
        yield
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing database connection")
        

with db_handler():
    print("Performing database operations")
