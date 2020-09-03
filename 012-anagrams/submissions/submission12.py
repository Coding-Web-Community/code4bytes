import argparse

x = lambda S, T: len(S) == len(T) and sorted(list(S)) == sorted(list(T))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(dest='arg1')
    parser.add_argument(dest='arg2')

    args = parser.parse_args()

    print(x(args.arg1, args.arg2))
