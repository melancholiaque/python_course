from sys import argv

def f():
    argc = len(argv)

    if argc == 3:
        with open(argv[1], 'r') as fd:
            print(sum(1 for line in fd if line.rstrip('\n') == argv[2]))
    elif argc == 4:
        with open(argv[1], 'r') as fd:
            lines = fd.readlines()
            new_lines = [f'{argv[3]}\n' if line.rstrip() == argv[2] else line
                         for line in lines]
        with open(argv[1], 'w') as fd:
            for line in new_lines:
                fd.write(line)
