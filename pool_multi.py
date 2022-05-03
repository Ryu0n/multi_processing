from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == '__main__':
    with Pool(processes=5) as p:
        print(p.map(f, [i for i in range(100000000)]))
