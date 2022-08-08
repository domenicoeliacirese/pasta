'''
Provides some utilities to print warnings and errors.
'''
import sys

YELLOW = '\33[93m'
RED = '\033[91m'
END = '\033[0m'


def print_error_and_exit(message : str):
    '''
    Prints the error message 'message' and exits.
    '''
    print(RED + "Error: " + message + END)
    sys.exit(-1)


def print_waring(message : str):
    '''
    Prints the warning message 'message'.
    '''
    print(YELLOW + "Warning: " + message + END)


def warning_prob_fact_twice(
    key : str,
    new_prob : float,
    old_prob : float
    ) -> None:
    '''
    Prints a warning to indicate a probabilistic fact defined twice.
    '''
    print(f"Probabilistic fact {key} already defined")
    print(f"with probability {old_prob}.")
    print(f"Trying to replace it with probability {new_prob}.")


def is_number(n: 'int|float|str') -> bool:
    try:
        float(n)
    except ValueError:
        return False
    return True
