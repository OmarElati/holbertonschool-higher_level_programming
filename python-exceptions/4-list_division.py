#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for items in range(list_length):
        try:
			x = my_list_1[items]
			y = my_list_2[items]
            if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
                raise TypeError("Wrong type")
            result = my_list_1[items] / my_list_2[items]
        except TypeError as e:
            print(e)
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        result_list.append(result)
    return result_list
