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
    # print("NextSpace: ", String[:String.find(" ")].strip())
    # print("finder: ", finder)
    if finder > 0:
        return String[:finder].strip()
    elif finder <= 0:
        return String

for line in f:
    print("Line: ", line)
    game = line[line.find(" ") + 1:line.find(":")]
    print("Game: ", game)
    line = line[line.find(": ") + 2:].replace(",", "").replace(";", "").strip()
    # print("next space: ", nextSpace(line))
    while line != "":
        result = nextSpace(line)
        print("Result: ", result)
        if result.isnumeric():
            blocks = int(result)
            line = line[line.find(" "):].strip()
            print("broken? ", line)
        elif result == "":
            print("elif: ", result == "")
            break
        else:
            color = result
            line = line.replace(color, "", 1).strip()
            print(line)
            if blocks > possible[color]:
                game = 0
                break

    sum += int(game)
print(sum)
