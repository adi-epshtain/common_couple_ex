from utils import find_most_common_couple
import logging as log
import coloredlogs


def main():
    coloredlogs.install(level='DEBUG')

    baskets = [['coke', 'ice', 'meat', 'ketchup', 'apple', 'banana'],
               ['coke', 'bread', 'meat', 'ketchup', 'apple', 'strawberry'],
               ['coke', 'pepsi', 'meat', 'ketchup', 'apple', 'banana'],
               ['pepsi', 'ice', 'meat', 'bread', 'tomato', 'cucumber'],
               ['sprite', 'rum', 'meat', 'ketchup', 'strawberry', 'banana']]

    results = find_most_common_couple(baskets)
    log.info(f"Results Are: {results}")


if __name__ == '__main__':
    main()
