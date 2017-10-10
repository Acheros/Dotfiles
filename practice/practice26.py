#!/usr/bin/python3

numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,   # noqa
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,      # noqa
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,   # noqa
        958, 743, 527
        ]

def get_number_list():                      # get number list_number
    list_number = []
    for i in numbers:
        number = int(i)
        list_number.append(number)
    return list_number


for i in get_number_list():                 # main function
    if i == 237:
        print(i)
        break
    else:
        print(i)
