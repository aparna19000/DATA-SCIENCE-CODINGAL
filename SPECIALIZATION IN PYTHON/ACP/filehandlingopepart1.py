# Method 1: Read entire file
print("Method 1: read()")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("-" * 30)

# Method 2: Read one line at a time
print("Method 2: readline()")
with open("sample.txt", "r") as file:
    print(file.readline())
    print(file.readline())

print("-" * 30)

# Method 3: Read all lines into a list
print("Method 3: readlines()")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

print("-" * 30)

# Method 4: Read file using a loop
print("Method 4: for loop")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())