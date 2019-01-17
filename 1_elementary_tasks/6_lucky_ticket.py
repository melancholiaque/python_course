from itertools import cycle, compress


d = {
    'Simple': (lambda arr: sum(arr[:3]) == sum(arr[-3:])),
    'Difficult': (lambda arr: sum(i for i in arr if i % 2 == 0) ==
                              sum(i for i in arr if i % 2 != 0)),
    'Mixed': (lambda arr: sum(compress(arr, cycle([0, 1]))) ==
                          sum(compress(arr, cycle([1, 0]))))
}

with open(input('input file: '), 'r') as fd:
    lines = fd.readlines()
    type_ = lines[0].rstrip()
    numbers = [list(map(int, l.rstrip())) for l in lines[1:]]
    f = d[type_]
    print(sum(1 for num in numbers if f(num)))
