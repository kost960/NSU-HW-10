import os

os.mkdir('simple')
with open('input.txt', 'r', encoding="utf-8") as f:
    x = f.readlines()
with open('simple\\output.txt', 'w', encoding="utf-8") as f:
    for number, line in enumerate(x):
        if (number + 1) % 2 == 0:
            f.write(line)
