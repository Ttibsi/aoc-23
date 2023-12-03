import re

def part1(lines):
    successful_games = []

    for line in lines:
        game = line.strip("\n").split(":")
        dice = game[1].split(";")


        for hand in dice:
            red = 0
            green = 0
            blue = 0
            clean_hand  = hand.rstrip().split(",")

            for i in clean_hand:
                count, colour = i[1:].split(" ")
                colour = colour.strip(",")

                if colour == "red":
                    red += int(count)
                elif colour == "green":
                    green += int(count)
                elif colour == "blue":
                    blue += int(count)

            if red <= 12 and green <= 13 and blue <= 14:
                game_val = game[0].split(" ")
                successful_games.append(int(game_val[1]))

    print(set(successful_games))
    print(sum(set(successful_games)))


def part2(lines):
    ...


def main():
    with open("input/day2.txt") as f:
        lines = f.readlines()

    part1(lines)

main()
