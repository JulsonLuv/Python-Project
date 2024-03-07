def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print("Content written to file successfully.")

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    print("***************************")
    print("Content read from file:")
    print(content)
    print("***************************")

def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + '\n')

    print("***************************")
    print("Content appended to file successfully.")

# Main program loop
while True:
    print("1. Write to file")
    print("2. Read from file")
    print("3. Append to file")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        file_name = input("Enter the file name: ")
        content = input("Enter the content to write to the file: ")
        write_to_file(file_name, content)
    elif choice == '2':
        file_name = input("Enter the file name: ")
        read_from_file(file_name)
    elif choice == '3':
        file_name = input("Enter the file name: ")
        content = input("Enter the content to append to the file: ")
        append_to_file(file_name, content)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting program.")