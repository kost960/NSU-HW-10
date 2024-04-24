with open('input.txt', 'r', encoding="utf-8") as f:
    x = f.readlines()
with (open('output.txt', 'w', encoding="utf-8") as f):
    for line in x:
        if len(line)-1 > 20:
            f.write(line)