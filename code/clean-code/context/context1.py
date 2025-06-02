
def stop_database():
    print("systemctl stop postgresql.")

def start_database():
    print("systemctl start postgresql.")
    
class DBHandler:
    def __enter__(self):
        print("DBHandler: Entering context, starting database.")
        start_database()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("DBHandler: Exiting context, stopping database.")
        stop_database()
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return True

def db_backup():
    print("Backing up database...")
    
def main():
    with DBHandler():
        db_backup()
        print("Database operations completed successfully.")

if __name__ == "__main__":
    main()