with open('input.txt', 'r', encoding="utf-8") as f:
    x = f.readlines()
with open('output.txt', 'w', encoding="utf-8") as f:
    for line in x:
        if line[0] == 'A' or line[0] == 'a':
            f.write(line)