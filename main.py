print("Hello World")

file1 = open("gradesv2.txt", "r")

some_lines = file1.readlines()

for lines in some_lines:
    lines = lines.split(',')
    avg = (int(lines[1]) + int(lines[2]) + int(lines[3])) / 3
    print(f"Name:{lines[0]}, GPA: {avg}")


    #this is an example that might help with the second project