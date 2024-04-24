for i in range(1, 4):
    with open(f'input{i}.txt', 'r', encoding="utf-8") as f:
        x = f.readlines()
    res = 0
    try:
        res = str((int(x[0]) / int(x[1])) + int(x[2]))
    except ValueError:
        res = 'data error'
    except ZeroDivisionError:
        res = 'division by 0'
    with (open(f'output{i}.txt', 'w', encoding="utf-8") as f):
        f.write(res)
