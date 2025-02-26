#!/usr/bin/env python3

import time

class AddedByIdList():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.ids = []
        return cls._instance

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
        if self.counter >= 29:
            print("Sleeping...")
            time.sleep(30)
            print("Continuing...")
        self.counter = 0
