#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __innit__(self, name="defaultName"):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if(type(name in (str) and ( 1<= len(name) <= 25))):
            return self._name
        else:
            print("Name must be string between 1 and 25 charachters.")
    pass

class Human:
    species = "Homo sapiens"

    def __init__(self, age):
        self.age = age

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        print(f"Setting age to { age }")
        self._age = age

    age = property(get_age, set_age)



    # reagan = Human("32")
