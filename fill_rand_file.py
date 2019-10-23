from random import randrange

def main():
    _range = 60
    number_of_lines = randrange(500, 1000)
    with open("input.txt", "w") as _f:
        _f.write(str(_range) + '\n')
        for line in range(number_of_lines):
            _f.write("{} {}\n".format(randrange(0, _range), randrange(0, _range)))

if __name__ == '__main__':
    main()