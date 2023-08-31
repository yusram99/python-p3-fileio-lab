def write_file(file_name, file_content):
    # Add the file extension
    file_name = str(file_name) + ".txt"      # Convert to string before concatenating
    with open(file_name, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
      # Add the file extension
    file_name = str(file_name) + ".txt"
    # Append content to the file
    with open(file_name, "a") as file:
        file.write(append_content + "\n")

def read_file(file_name):
    # Add the file extension
    file_name = str(file_name) + ".txt"
    
    # Read content from the file
    with open(file_name, "r") as file:
        content = file.read()
    return content

# Example usage
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

file_content = read_file(file_name="logfile")
print(file_content)
