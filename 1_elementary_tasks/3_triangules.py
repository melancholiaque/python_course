from math import sqrt

ts = []


def V(a, b, c):
    p = a+b+c/2
    return sqrt(p * (p-a) * (p-b) * (p-c))


while True:
    name = input('name: ')
    edges = [float(input(f'edge {edge}: ')) for edge in 'abc']
    ts.append([name, *edges])
    if not input('continue? [y]es\n').lower() in ['y', 'yes']:
        break

for name, a, b, c in sorted(ts, key=lambda x: -V(*x[1:])):
    print(f'[Triangle {name}]: {V(a,b,c)} cm')
