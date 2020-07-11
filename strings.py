f = open("file.txt", "r")
counter = 0
word = ""
for line in f:
    if line:
        counter += 1
    if word in line:
        print(counter)
        print(line.rstrip())
f.close()

