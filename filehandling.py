def main():
    try:
        # File Creation
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("This is line 3 with some numbers: 56789\n")

        # File Reading and Display
        print("Contents of my_file.txt:")
        with open("my_file.txt", "r") as file:
            for line in file:
                print(line.strip())

        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("This is line 4 appended.\n")
            file.write("Another line with more text.\n")
            file.write("Final line, goodbye!\n")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script execution completed.")

if __name__ == "__main__":
    main()
