#!/usr/bin/python3
result_list = []


def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            x = my_list_1[i]
            y = my_list_2[i]
            a = isinstance(x, (int, float))
            b = isinstance(y, (int, float))
            if not a or not b:
                raise TypeError("wrong type")
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
