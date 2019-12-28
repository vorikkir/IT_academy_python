#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import hashlib
from random import shuffle


def get_names_gen():
    """Unique name generator"""
    total = set()
    result = None
    while True:
        num = yield result
        letters = list("qwertyuiopasdfghjklzxcvbnm")
        shuffle(letters)
        letters = "".join(letters)[0]
        result = hashlib.md5(str.encode(num)).hexdigest().rjust(33, letters) + f.name[-4:]
        if result in total:
            continue
        else:
            total.add(result)


if __name__ == '__main__':
    names = get_names_gen()
    next(names)

    with open("img.jpg") as f:
        print(names.send(f.name))

    with open("cat.jpg") as f:
        print(names.send(f.name))

    with open("dog.jpg") as f:
        print(names.send(f.name))
