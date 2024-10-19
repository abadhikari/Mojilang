from enum import Enum


class BlockScope(Enum):
    FUNCTION = "FUNCTION"
    LOOP = "LOOP"
    DEFAULT = "DEFAULT"
