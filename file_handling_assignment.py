# Task 1 - File Creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
            file.write("The answer is 42.\n")
        print("File created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 2 -  File Reading and Display
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 3- File Appending
def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is appended text.\n")
            file.write("More text is being appended.\n")
            file.write("The final answer is still 42.\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 4: Error Handling
def main():
    try:
        create_file()
        read_file()
        append_to_file()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File handling operations complete.")

if __name__ == "__main__":
    main()