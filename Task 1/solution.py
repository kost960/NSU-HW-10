x = ''
with open('input.txt', 'r', encoding="utf-8") as f:
    x = f.read().upper()
    print(x)
with open('output.txt', 'w', encoding="utf-8") as f:
    f.write(x)