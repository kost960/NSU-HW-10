with open('input.txt', 'r', encoding="utf-8") as f:
    x = f.readlines()
with open('output.txt', 'w', encoding="utf-8") as f:
    for line in x:
       f.write(line[0])