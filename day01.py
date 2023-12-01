import re

def part1(lines):
    sum = 0

    for line in lines:
        num = ""

        for ch in line:
            if ch.isdigit():
                num += ch
                break

        for ch in reversed(line):
            if ch.isdigit():
                num += ch
                break

        num = int(num)
        sum += num

    print(sum)


def word_to_num(w) -> int:
    if w == "one":
        return 1 
    elif w == "two":
        return 2 
    elif w == "three":
        return 3
    elif w == "four":
        return 4 
    elif w == "five":
        return 5 
    elif w == "six":
        return 6 
    elif w == "seven":
        return 7 
    elif w == "eight":
        return 8 
    elif w == "nine":
        return 9 
    else:
        return int(w)


def part2(lines):
    sum = 0

    for line in lines:
        num = ""
        m = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
        num += str(word_to_num(m[0]))
        num += str(word_to_num(m[-1]))

        sum += int(num)

    print(sum)


def main():
    with open("input/day1.txt") as f:
        lines = f.readlines()

    part2(lines)

main()
