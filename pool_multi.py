from multiprocessing import Pool


def f(x):
    return x * x


def f2(x, y):
    return x + y


if __name__ == '__main__':
    with Pool(processes=5) as p:
        print(p.map(f, [i for i in range(100000000)]))

    with Pool(processes=2) as p:
        print(p.starmap(f2, [(i, i) for i in range(10)]))
