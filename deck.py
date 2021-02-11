from random import randrange
def strat():
        with open("deck.txt") as f:
            data = f.readlines()
            return data[randrange(len(data))].strip()
if __name__ == "__main__":
    print()
    print(strat())
    print()
