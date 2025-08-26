# File Read & Write Challenge

try:
    # Read the file
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    # Modify the content (e.g., add line numbers)
    modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

    # Write to new file
    with open("output.txt", "w") as outfile:
        outfile.writelines(modified_lines)

    print("File successfully modified and saved to output.txt")

except FileNotFoundError:
    print("The file 'input.txt' was not found.")

