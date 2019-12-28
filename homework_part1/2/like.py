#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
1. likes() -> "no one likes this"
2. likes("Peter") -> "Peter likes this"
3. likes("Jacob", "Alex") -> "Jacob and Alex like this"
4. likes("Max", "John", "Mark") -> "Max, John and Mark like this"
5. likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
"""


def likes(*arr: str):
    if len(arr) == 0:
        print("no one likes this")
    elif len(arr) == 1:
        print(f"{arr[0]} likes this")
    elif len(arr) == 2:
        print(f"{arr[0]} and {arr[1]} like this")
    elif len(arr) == 3:
        print(f"{arr[0]}, {arr[1]} and {arr[2]} like this")
    elif len(arr) > 3:
        print(f"{arr[0]}, {arr[1]} and {len(arr) - 2} others like this")


if __name__ == '__main__':
    likes("Alex", "Jacob", "Mark", "Max")
