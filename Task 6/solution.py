for i in range(1, 4):
    with open(f'input{i}.txt', 'r', encoding="utf-8") as f:
        x = f.readlines()
        print(x)
    with (open(f'output{i}.txt', 'w', encoding="utf-8") as f):
        try:
            if int(x[0]) == len(x) - 1:
                f.write('YES')
            else:
                f.write('NO')
        except ValueError:
            f.write('ERROR')
