# Functions and exceptions practice

1. Write function according to following signature _print_range(begin: int, end:int, reverse: bool = False)_ that prints range of numbers from begin to end to the screen. If reverse is True then function should print numbers from end to begin.

2. Write function according to following signature get_range_numbers(begin: int, end: end, even: bool = True) -> list. 
If even is True function return list of even numbers, elese odd numbers.

3. Write funtion random_list(begin: int, end: int, amount: int, exclude: list = None) that creates and returns list of given amount with randomly selected elements excluding those that were given in exclude list. 

4. Add new argument to random_list that is called unique: bool that will be responsible for leaving only unique elements in your random list. For example there will never be list like [9, 9, 1, 0] if you switch this option to true. 
