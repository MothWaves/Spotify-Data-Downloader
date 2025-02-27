#!/usr/bin/env python3

import time

class AddedByList():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.ids = []
        return cls._instance

    def get_display_names(self):
        requests_counter = RequestsCounter()
        sp = SpotifySingleton()
        self.display_names = {}

        for identifier in self.ids:
            requests_counter.check_rate()
            self.display_names[identifier] = sp.user(identifier)['display_name']
            requests_counter.increment()

class RequestsCounter():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0
        return cls._instance

    def increment(self):
        self.counter += 1

    def check_rate(self):
        if self.counter >= 50:
            print("Sleeping...")
            time.sleep(10)
            print("Continuing...")
            self.counter = 0

class SpotifySingleton():
    _instance = None

    # This is an awful terrible bastardization of the singleton pattern.
    # I apologize to anyone looking at this.
    # That being said, Works wonderfully :)
    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = args[0]
        return cls._instance
