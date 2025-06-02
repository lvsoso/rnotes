import contextlib

class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        print("Opening database connection")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An error occurred: {exc_value}")
        print("Closing database connection")


# 自动在上下文中运行
@dbhandler_decorator()
def perform_db_operations():
    print("Performing database operations")
    # raise ValueError("Simulated error")  # Uncomment to test error handling
    print("Database operations completed successfully")
    

if __name__ == "__main__":
    perform_db_operations()
    print("Main function completed")
