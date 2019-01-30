def f():
    while True:
        a, b, c, d = [float(input(f'{e}: ')) for e in 'abcd']
        if (a <= c and b <= d) or (b <= c and a <= d):
            print(True)
        else:
            print(False)
        if not input('continue? [y]es\n').lower() in ['y', 'yes']:
            break
