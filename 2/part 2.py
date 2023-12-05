input = "input.txt"
sum = 0

possible = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

f = open(input, "r")

def nextSpace( String ):
    finder = String.find(" ")
    if finder > 0:
        return String[:finder].strip()
    elif finder <= 0:
        return String

for line in f:
    game = line[line.find(" ") + 1:line.find(":")]
    line = line[line.find(": ") + 2:].replace(",", "").replace(";", "").strip()
    while line != "":
        result = nextSpace(line)
        if result.isnumeric():
            blocks = int(result)
            line = line[line.find(" "):].strip()
        elif result == "":
            break
        else:
            color = result
            line = line.replace(color, "", 1).strip()
            if blocks > possible[color]:
                game = 0
                break

    sum += int(game)
print(sum)
