"""
run the main app
"""
from .euclid import Euclid


def run() -> None:
    reply = Euclid().run()
    print(reply)
