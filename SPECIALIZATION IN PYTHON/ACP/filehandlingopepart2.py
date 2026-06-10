import os

# 1. Create and Write to a file
file = open("sample.txt", "w")
file.write("Hello World!\n")
file.write("Welcome to Python File Handling.\n")
file.close()

print("Data written successfully.")

# 2. Read the file
file = open("sample.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()

# 3. Append data to the file
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

print("\nData appended successfully.")

# 4. Read updated file
file = open("sample.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()

# 5. Rename the file
os.rename("sample.txt", "new_sample.txt")
print("\nFile renamed successfully.")

# 6. Delete the file
os.remove("new_sample.txt")
print("File deleted successfully.")