#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division_results = []  # creates a list to store the divisionresults

    for i in range(list_length):
        try:
            # attempt to perform the division
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            # handle specific exceptions that might occur
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0  # set result to 0 in case of error
        finally:
            # append the result to the list, regardless of erro
            division_results.append(result)
    return division_results  # return the list of  division results
