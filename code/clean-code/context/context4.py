import contextlib

with contextlib.suppress(FileNotFoundError):
    print("Attempting to read a file that may not exist...")
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
