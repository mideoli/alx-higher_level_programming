#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
