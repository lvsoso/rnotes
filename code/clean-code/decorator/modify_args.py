# src/decorator_universal_1.py
from functools import wraps


class DBDriver:
    def __init__(self, dbstring: str) -> None:
        self.dbstring = dbstring

    def execute(self, query: str) -> str:
        return f"query {query} at {self.dbstring}"

def inject_db_driver(function):
    """This decorator converts the parameter by creating a ``DBDriver``
    instance from the database dsn string.
    """
    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))
    return wrapped

@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


if __name__ == '__main__':
    print(run_query('test_ok'))