# i) Write the text to a file named code.txt
with open("code.txt", "w") as file:
    file.write("PROGRAMMING IN PYTHON")

# ii) Read the text from the file and print it
with open("code.txt", "r") as file:
    content = file.read()
    print(content)
