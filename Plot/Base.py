#!/usr/bin/python3


class Base():
    def __init__(self, name):
        self.name = name


    def print(self):
        print("My name is {}".format(self.name))
