#!/usr/bin/env python3

if __name__ == '__main__':
 name = input('Hello, what is your name? ')

year_now = int(input('what year is it today?' ))
year_born = int(input('and what year were you born? '))

age = year_now - year_born

print(f'hello, {name}. it is good to meet you. This year you will be {age} years old.')