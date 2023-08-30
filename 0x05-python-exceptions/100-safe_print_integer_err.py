#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except ValueError as ve:
        error_message = "Exception: {}".format(ve)
        print(error_message, file=sys.stderr)
        return False
