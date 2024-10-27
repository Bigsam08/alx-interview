#!/usr/bin/python3
'''pass loger count, status codes and error
handlingling + ctrl C after 10 lines '''
import sys


def print_stats(stats, file_size):
    print("File size: {:d}".format(file_size))
    for code, count in sorted(stats.items()):
        if count:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    count = 0
    file_size = 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    stats = {code: 0 for code in codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass

            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)

    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
    