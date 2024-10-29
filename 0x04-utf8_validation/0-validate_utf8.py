#!/usr/bin/python3
''' A validUTF* function to check if int and the type of byte '''


def validUTF8(data):
    ''' check if integers are utf-8 validated '''
    next = 0
    dataLen = len(data)
    for i in range(dataLen):
        if next > 0:
            next -= 1
            continue
        if type(data[i]) is not int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            next = 0
        elif data[i] & 0b11111000 == 0b11110000:
            byte = 4
            if dataLen - 1 >= byte:
                ff = list(map(
                    lambda X: X & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                    ))
                if not all(ff):
                    return False
                next = byte - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            byte = 3
            if dataLen - 1 >= byte:
                ff = list(map(
                    lambda X: X & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                    ))
                if not all(ff):
                    return False
                next = byte - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            byte = 2
            if dataLen - 1 >= byte:
                ff = list(map(
                    lambda X: X & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                    ))
                if not all(ff):
                    return False
                next = byte - 1
            else:
                return False
        else:
            return False
    return True
