from enum import Enum


class Token(int, Enum):
    BOT = 9225
    LINEBREAK = 13
    SYSTEM = 1788
    USER = 1404
