#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, {}!".format(name))

greet("Guido")



def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))

# Example usage
greet_with_default()  # Output: Hello, programmer!
greet_with_default("John")  # Output: Hello, John!


def add(num1, num2):
    result = num1 + num2
    return result


def halve(number):
    result = number / 2
    return result
