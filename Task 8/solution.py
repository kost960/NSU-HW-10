with open('input.txt', 'r', encoding="utf-8") as f:
    x = list(map(int, f.read().splitlines()))
with open('output.txt', 'w', encoding="utf-8") as f:
    average_january = sum(x[0:31]) / 31
    average_february = sum(x[31:59]) / 28
    average_march = sum(x[59:90]) / 31
    average_april = sum(x[90:120]) / 30
    average_may = sum(x[120:151]) / 31
    average_june = sum(x[151:181]) / 30
    average_july = sum(x[181:212]) / 31
    average_august = sum(x[212:243]) / 31
    average_september = sum(x[243:273]) / 30
    average_october = sum(x[273:304]) / 31
    average_november = sum(x[304:334]) / 30
    average_december = sum(x[334:365]) / 31
    f.write(
        f'{average_january:.0f}\n{average_february:.0f}\n{average_march:.0f}\n{average_april:.0f}\n{average_may:.0f}\n'
        f'{average_june:.0f}\n{average_july:.0f}\n{average_august:.0f}\n{average_september:.0f}\n'
        f'{average_october:.0f}\n{average_november:.0f}\n{average_december:.0f}\n')
