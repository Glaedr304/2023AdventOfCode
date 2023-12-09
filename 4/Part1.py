input = "input.txt"

output = 0

f = open(input, "r")

for line in f:
    card = line[line.find(" "):line.find(":")]
    line = line[line.find(":") + 1:].strip()

    WinningNumbers = eval( "(" + line[:line.find("|")].replace("  ", " ").strip().replace(" ", ",") + ")")
    Numbers = eval( "(" + line[line.find("|") + 1:].replace("  ", " ").strip().replace(" ", ",") + ")")

    winners = 0

    for x in WinningNumbers:
        if x in Numbers:
            winners += 1
    if winners > 0:
        output += 2**(winners - 1)


print("Output: ", output)
