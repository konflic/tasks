# Functions and exceptions practice session

1. Write function according to following signature _print_range(begin: int, end:int, reverse: bool = False)_ that prints range of numbers from begin to end to the screen. If reverse is True then function should print numbers from end to begin.

```python
print_range(10, 15, True)
>>> 15
>>> 14
>>> 13
>>> 12
>>> 11
>>> 10
```

2. Write function according to following signature _get_range_numbers(begin: int, end: end, even: bool = True) -> list_. 
If even is True function return list of even numbers, elese odd numbers.

```python
range_list = get_range_numbers(1, 10)
print(range_list)
>>> [2, 4, 6, 8, 10]
```

3. Write funtion _random_list(begin: int, end: int, amount: int, exclude: list = None) -> list_ that creates and returns list of given amount with randomly selected elements excluding those that were given in exclude list. 

```python
rnd_list = random_list(1, 20, 5, [4, 1])
print(rnd_list)
>>> [3, 11, 5, 3, 9]
```

4. Add new argument to _random_list_ that is called unique: bool that will be responsible for leaving only unique elements in your random list. For example there will never be list like [9, 9, 1, 0] if you switch this option to True. 

5. Write function _is_palindrome(word: str) -> bool_ that checks if word is palindrome.

```python
is_palindrome("aba")
>>> True
is_palindrome("what?")
>>> False
```

6. Write function _add_separator(string: str, separator: str) -> str_ that adds separator to each word of given string, but ignores spaces and special characters like ".", or "-", separator should be aded only into words. Word should not start or end with separator.

```python
add_separator("Hello", "*")
>>> H*e*l*l*o
add_separator("Hey, how are you?")
>>> H*e*y, h*o*w a*r*e y*o*u?
```
